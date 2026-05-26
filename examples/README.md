
---

### 5. `examples/` Folder README

**Path:** `examples/README.md`

```markdown
# Examples Directory - Jupyter Notebooks & Interactive Demos

This directory contains interactive Jupyter notebooks demonstrating key concepts from *Defending Tomorrow*.

## 📁 Structure

| Subfolder | Purpose | Example Content |
|-----------|---------|-----------------|
| `notebooks/` | Interactive demonstrations | Live code, visualizations, tutorials |

## 📓 Available Notebooks (Planned)

| Notebook | Chapter | Description |
|----------|---------|-------------|
| `fgsm_tutorial.ipynb` | 3 | Step-by-step adversarial example generation |
| `differential_privacy_demo.ipynb` | 4 | Visualizing privacy guarantees |
| `drift_detection.ipynb` | 5 | Real-time model drift monitoring |
| `prompt_injection_lab.ipynb` | 6 | Interactive prompt injection testing |
| `zero_trust_ai_simulator.ipynb` | 12 | Policy simulation environment |

## 🚀 Running Notebooks

### Local Setup:
```bash
# From repository root
pip install -r requirements.txt
pip install jupyter


# Navigate to examples
cd examples/notebooks
jupyter notebook
Online (GitHub Codespaces):
Click "Code" → "Codespaces" → "Create codespace"

Wait for environment to build

Open any .ipynb file

📖 Interactive Learning Path
Recommended order for hands-on practice:

Beginner → FGSM tutorial (Chapter 3)

Intermediate → Drift detection (Chapter 5)

Advanced → Zero trust simulator (Chapter 12)

⚠️ Environment Requirements
Python 3.9+

8GB RAM minimum (16GB recommended for LLM examples)

GPU optional but helpful for deep learning notebooks
