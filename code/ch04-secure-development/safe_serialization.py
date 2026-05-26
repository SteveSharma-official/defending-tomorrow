"""
Code 4.3: Safe Model Serialization with safetensors
Defending Tomorrow - Chapter 4: Secure Model Development

Demonstrates secure model saving/loading to avoid pickle deserialization attacks.
"""

import torch
import torch.nn as nn
from safetensors.torch import save_file, load_file
import json
import tempfile
import os

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 5)
    
    def forward(self, x):
        return self.fc(x)

def safe_save_model(model: nn.Module, path: str, metadata: dict = None):
    """
    Save model safely using safetensors format.
    No pickle, no arbitrary code execution risk.
    """
    # Extract state dict as tensors
    state_dict = model.state_dict()
    
    # Convert to plain Python dict of tensors
    tensor_dict = {k: v.cpu() for k, v in state_dict.items()}
    
    # Save with optional metadata
    save_file(tensor_dict, path, metadata=metadata or {})
    print(f"[✓] Model saved safely to {path}")

def safe_load_model(model: nn.Module, path: str):
    """
    Load model safely from safetensors format.
    """
    # Load tensors (safe - no code execution)
    tensor_dict = load_file(path)
    
    # Load into model
    model.load_state_dict(tensor_dict, strict=True)
    print(f"[✓] Model loaded safely from {path}")
    return model

def unsafe_pickle_demo():
    """Demonstrate why pickle is dangerous (conceptual)."""
    print("\n[!] WARNING: pickle.load() can execute arbitrary code!")
    print("    A malicious .pth file could contain __reduce__ exploits.")
    print("    Always prefer safetensors for untrusted models.\n")

if __name__ == "__main__":
    print("=== Safe Model Serialization with safetensors ===\n")
    
    # Create and train a dummy model
    model = SimpleModel()
    model.eval()
    
    # Save safely
    with tempfile.NamedTemporaryFile(suffix=".safetensors", delete=False) as f:
        safe_save_model(model, f.name, metadata={"author": "Defending Tomorrow", "version": "1.0"})
        temp_path = f.name
    
    # Load safely
    loaded_model = SimpleModel()
    safe_load_model(loaded_model, temp_path)
    
    # Verify
    test_input = torch.randn(1, 10)
    original_output = model(test_input)
    loaded_output = loaded_model(test_input)
    
    assert torch.allclose(original_output, loaded_output)
    print(f"\n[✓] Verification passed: outputs match")
    
    # Clean up
    os.unlink(temp_path)
    
    unsafe_pickle_demo()
