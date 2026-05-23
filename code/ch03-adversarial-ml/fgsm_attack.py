"""
Adversarial example generation using FGSM (Fast Gradient Sign Method).
From Chapter 3 of "Defending Tomorrow" by Steve Sharma.

This is a placeholder implementation. Full code will be released
alongside the book publication.
"""

import torch
import torch.nn as nn

def fgsm_attack(model, images, labels, epsilon):
    """Generate adversarial examples using FGSM."""
    images.requires_grad = True
    outputs = model(images)
    loss = nn.CrossEntropyLoss()(outputs, labels)
    model.zero_grad()
    loss.backward()
    perturbations = epsilon * images.grad.sign()
    adversarial_images = images + perturbations
    return torch.clamp(adversarial_images, 0, 1)

if __name__ == "__main__":
    print("FGSM attack module ready.")
    print("Full implementation coming with the book release.")
