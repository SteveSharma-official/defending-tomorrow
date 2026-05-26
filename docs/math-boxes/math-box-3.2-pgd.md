# Math Box 3.2: Projected Gradient Descent (PGD)

## Iterative Update Rule

$$x^{t+1} = \Pi_{x + \mathcal{S}} \left( x^t + \alpha \cdot \text{sign}(\nabla_x J(\theta, x^t, y)) \right)$$

## Where:
- $x^{t}$ = input at iteration $t$ (starting with $x^0 = x$)
- $\alpha$ = step size per iteration (small, e.g., 0.01)
- $\Pi_{x + \mathcal{S}}$ = projection operator onto the $\ell_\infty$ ball of radius $\epsilon$ around $x$
- $\mathcal{S} = \{ \delta : \|\delta\|_\infty \le \epsilon \}$ = allowed perturbation set
- All other symbols same as FGSM

## Comparison to FGSM

| Feature | FGSM | PGD |
|---------|------|-----|
| Steps | Single | Multiple (e.g., 40) |
| Strength | Weaker | Stronger (state-of-the-art) |
| Computation | Fast | Slower |
| Use case | Quick estimation | Robustness benchmarking |

## Projection Step

After each update, projection ensures the perturbation stays within the $\epsilon$ budget:

$$\Pi_{x + \mathcal{S}}(z) = \min(\max(z, x - \epsilon), x + \epsilon)$$

Element-wise clipping to the range $[x_i - \epsilon, x_i + \epsilon]$.

## Why PGD is Stronger

PGD takes multiple small steps, allowing it to find better local maxima of the loss function. It is considered the benchmark for evaluating adversarial robustness.

$$\text{FGSM} \subset \text{PGD with } T=1$$

As number of steps $T \to \infty$, PGD converges to the optimal attack within the $\epsilon$ ball.
