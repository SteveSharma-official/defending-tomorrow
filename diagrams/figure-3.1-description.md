# Figure 3.1: High-Dimensional Vulnerability Visualization

## Concept

This diagram illustrates why neural networks are vulnerable to adversarial examples in high-dimensional spaces.

## Visual Description

**Left panel – Low-dimensional intuition (2D):**
- A simple decision boundary (curved line) separating two classes
- A data point far from the boundary, with a small arrow showing a perturbation that stays within the same class region
- Caption: "In 2D, random perturbations rarely cross decision boundaries"

**Right panel – High-dimensional reality (shown as 3D with "many dimensions" notation):**
- The same data point is now surrounded by a "thin shell" of adversarial directions
- Multiple arrows pointing in different directions, many crossing decision boundaries
- An annotation showing that volume scales exponentially: "Available adversarial directions ≈ (2ε)^d"
- Caption: "In high dimensions, a small L∞ ball contains directions that cross boundaries"

## Key Insight

The model's input space has hundreds or thousands of dimensions. An ε-ball around any point contains a combinatorial number of directions, and many of those directions align with the gradient to fool the network.

## Related Equation

Volume ratio between ε-ball and the unit cube:

$$ \text{Volume}(\text{ball}) = \frac{\pi^{d/2}}{\Gamma(d/2+1)} \epsilon^d $$

For large d, most volume is near the surface (the "thin shell"), making adversarial directions abundant.
