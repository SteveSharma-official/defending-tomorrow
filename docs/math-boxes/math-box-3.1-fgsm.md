# Math Box 3.1: The Fast Gradient Sign Method (FGSM)

## Equation

$$x' = x + \epsilon \cdot \text{sign}(\nabla_x J(\theta, x, y))$$

## Where:
- $x$ = original input (e.g., image pixels)
- $x'$ = adversarial input
- $\epsilon$ = perturbation magnitude (small, e.g., 0.07)
- $\text{sign}()$ = element-wise sign function (-1, 0, or +1)
- $\nabla_x J$ = gradient of loss $J$ with respect to input $x$
- $\theta$ = model parameters
- $y$ = true label

## Intuition

The gradient $\nabla_x J$ points in the direction of *increasing* loss. By taking a small step $\epsilon$ in that direction, we slightly modify the input to confuse the model while keeping the change imperceptible to humans.

## Why It Works

Neural networks learn linear decision boundaries in high-dimensional spaces. A small perturbation aligned with the gradient can push an input across the decision boundary, changing the classification.

## Example

For an image classifier with 0-255 pixel values and $\epsilon = 10$, the attack adds or subtracts up to 10 from each pixel based on the sign of the gradient.

$$x'_{pixel} = x_{pixel} + 10 \cdot \text{sign}(\nabla_{pixel} J)$$

The resulting image looks identical to humans but fools the network.
