"""
Code 3.4: Adversarial Training Loop Skeleton
Defending Tomorrow - Chapter 3: Adversarial Machine Learning

A template for making models robust by training on adversarial examples.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from typing import Callable

def fgsm_attack(model, loss_fn, input_data, label, epsilon):
    """Fast Gradient Sign Method attack."""
    input_data.requires_grad = True
    output = model(input_data)
    loss = loss_fn(output, label)
    model.zero_grad()
    loss.backward()
    perturbation = epsilon * input_data.grad.sign()
    return input_data + perturbation

def adversarial_train_epoch(
    model: nn.Module,
    train_loader: DataLoader,
    optimizer: optim.Optimizer,
    loss_fn: nn.Module,
    epsilon: float,
    alpha: float = 0.5
) -> float:
    """
    Train for one epoch using adversarial training.
    
    Args:
        alpha: Balance between clean loss (0) and adversarial loss (1)
    """
    model.train()
    total_loss = 0.0
    
    for batch_x, batch_y in train_loader:
        # Standard forward pass
        clean_output = model(batch_x)
        clean_loss = loss_fn(clean_output, batch_y)
        
        # Generate adversarial examples
        adv_x = fgsm_attack(model, loss_fn, batch_x.clone(), batch_y, epsilon)
        adv_output = model(adv_x)
        adv_loss = loss_fn(adv_output, batch_y)
        
        # Combined loss
        loss = (1 - alpha) * clean_loss + alpha * adv_loss
        
        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    return total_loss / len(train_loader)


def evaluate_robustness(
    model: nn.Module,
    test_loader: DataLoader,
    loss_fn: nn.Module,
    epsilon: float
) -> dict:
    """Evaluate model on clean and adversarial examples."""
    model.eval()
    clean_correct = 0
    adv_correct = 0
    total = 0
    
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            # Clean accuracy
            clean_output = model(batch_x)
            clean_correct += (clean_output.argmax(1) == batch_y).sum().item()
            
            # Adversarial accuracy (using model's own gradients)
            batch_x.requires_grad = True
            adv_output = model(batch_x)
            loss = loss_fn(adv_output, batch_y)
            model.zero_grad()
            loss.backward()
            perturbation = epsilon * batch_x.grad.sign()
            adv_x = batch_x + perturbation
            adv_x = torch.clamp(adv_x, 0, 1)
            
            final_output = model(adv_x)
            adv_correct += (final_output.argmax(1) == batch_y).sum().item()
            total += batch_y.size(0)
    
    return {
        "clean_accuracy": clean_correct / total,
        "adversarial_accuracy": adv_correct / total,
        "robustness_gap": (clean_correct - adv_correct) / total
    }


if __name__ == "__main__":
    print("Adversarial Training Skeleton")
    print("Use with your own dataset and model architecture.")
    
    # Template for full training loop
    print("""
    # Full training loop example:
    
    for epoch in range(num_epochs):
        train_loss = adversarial_train_epoch(
            model, train_loader, optimizer, loss_fn, 
            epsilon=0.07, alpha=0.5
        )
        
        if epoch % eval_every == 0:
            metrics = evaluate_robustness(model, test_loader, loss_fn, epsilon=0.07)
            print(f"Epoch {epoch}: Clean={metrics['clean_accuracy']:.3f}, "
                  f"Adversarial={metrics['adversarial_accuracy']:.3f}")
    """)
