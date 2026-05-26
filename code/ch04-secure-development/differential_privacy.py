"""
Code 4.1: Differential Privacy Implementation with Opacus
Defending Tomorrow - Chapter 4: Secure Model Development

Demonstrates training a PyTorch model with differential privacy guarantees.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from opacus import PrivacyEngine
from opacus.validators import ModuleValidator

# Simple model for demonstration
class SimpleClassifier(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=128, num_classes=10):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        return self.fc2(x)

def train_dp_model(
    train_loader: DataLoader,
    epsilon: float = 3.0,
    delta: float = 1e-5,
    max_grad_norm: float = 1.0,
    epochs: int = 3,
    learning_rate: float = 0.01
):
    """Train a model with differential privacy."""
    
    model = SimpleClassifier()
    
    # Validate model for DP compatibility
    if not ModuleValidator.is_valid(model):
        model = ModuleValidator.fix(model)
    
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)
    loss_fn = nn.CrossEntropyLoss()
    
    # Attach privacy engine
    privacy_engine = PrivacyEngine()
    model, optimizer, train_loader = privacy_engine.make_private(
        module=model,
        optimizer=optimizer,
        data_loader=train_loader,
        noise_multiplier=1.0,
        max_grad_norm=max_grad_norm,
    )
    
    # Training loop
    model.train()
    for epoch in range(epochs):
        total_loss = 0.0
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            output = model(batch_x)
            loss = loss_fn(output, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        # Get epsilon spent so far
        spent_epsilon = privacy_engine.get_epsilon(delta)
        print(f"Epoch {epoch+1}: Loss={total_loss/len(train_loader):.4f}, "
              f"ε={spent_epsilon:.2f} (δ={delta})")
    
    return model, spent_epsilon

if __name__ == "__main__":
    print("=== Differential Privacy Demo ===")
    
    # Generate synthetic data
    X = torch.randn(1000, 1, 28, 28)
    y = torch.randint(0, 10, (1000,))
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=32)
    
    print(f"Target privacy budget: ε=3.0, δ=1e-5")
    model, final_epsilon = train_dp_model(loader, epsilon=3.0)
    print(f"\nTraining complete. Final ε={final_epsilon:.2f}")
    
    print("\n[✓] Model trained with differential privacy guarantee")
