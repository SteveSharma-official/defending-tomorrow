
---

### 6. `scripts/` Folder README

**Path:** `scripts/README.md`

```markdown
# Scripts Directory - Utility & Automation Tools

This directory contains standalone utility scripts for AI security automation, monitoring, and assessment.

## 📜 Available Scripts (Planned)

| Script | Purpose | Usage |
|--------|---------|-------|
| `generate_sbom.py` | Create SBOM for ML environments | `python generate_sbom.py --path ./model` |
| `model_checksum.py` | Verify model integrity | `python model_checksum.py --model model.pt` |
| `drift_detector.py` | Monitor data/concept drift | `python drift_detector.py --config config.yaml` |
| `api_extraction_detector.py` | Detect model extraction attempts | `python api_extraction_detector.py --logs access.log` |
| `checklist_merger.py` | Combine multiple checklists | `python checklist_merger.py --files *.md --output master.pdf` |

## 🛠️ Installation

Most scripts are standalone Python files with minimal dependencies:

```bash
# Install common dependencies
pip install pyyaml click rich

# Or use main requirements
pip install -r ../requirements.txt

