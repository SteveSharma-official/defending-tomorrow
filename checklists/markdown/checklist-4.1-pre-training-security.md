# Checklist 4.1: Pre-Training Security Checklist

## Project: _________________  Date: _________________

### Section A: Data Governance (6 items)
- [ ] Data provenance documented (origin, collection method, timestamp)
- [ ] Sensitive data identified (PII, PHI, financial, classified)
- [ ] Data licensing verified for commercial use
- [ ] Data sanitization applied (removal of PII, poisoning detection)
- [ ] Differential privacy budget defined (ε, δ)
- [ ] Data versioning/lineage tracking implemented

### Section B: Environment Security (5 items)
- [ ] Training environment isolated from production
- [ ] Network segmentation enforced (no direct internet access to training cluster)
- [ ] Access control: least privilege for data scientists
- [ ] Secrets management configured (API keys, credentials in vault)
- [ ] Code signing for training scripts

### Section C: Supply Chain Verification (4 items)
- [ ] Base images/containers from verified sources
- [ ] Dependency SBOM generated and reviewed
- [ ] Pre-trained model provenance verified (hash check)
- [ ] No known vulnerabilities in ML libraries (Snyk/safety scan)

### Section D: Experiment Tracking (3 items)
- [ ] MLflow/Weights & Biases secured with authentication
- [ ] Hyperparameters and code version logged
- [ ] Random seeds recorded for reproducibility

### Sign-off
- [ ] Security review completed
- [ ] Data privacy impact assessment done
- [ ] Training approved to proceed

**Reviewer:** _________________  **Date:** _________________
