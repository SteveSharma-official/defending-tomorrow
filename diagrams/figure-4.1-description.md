# Figure 4.1: Secure Data Lifecycle Architecture

## Visual Description

A horizontal flow diagram showing six stages with security controls at each step:

**Stage 1: Data Ingestion**
- Sources: Databases, APIs, Data Lakes, External Feeds
- Security: Provenance verification, TLS encryption

**Stage 2: Data Validation**
- Actions: Schema validation, outlier detection, poisoning scanning
- Security: Checksum verification, anomaly detection

**Stage 3: Data Sanitization**
- Actions: PII removal/masking, differential privacy injection
- Security: Secure enclave processing, access logging

**Stage 4: Data Labeling**
- Actions: Human/AI labeling, consensus verification
- Security: Labeler isolation, adversarial label detection

**Stage 5: Training Dataset**
- Storage: Encrypted at rest (AES-256)
- Security: Access controls (ABAC), immutable audit log

**Stage 6: Versioned Dataset**
- Actions: Immutable snapshot, lineage tracking
- Security: Cryptographic signing, retention policy

## Cross-cutting Controls (shown as vertical bars)

- **Encryption:** At rest + in transit + in use (confidential computing)
- **Access Control:** Least privilege + MFA + session recording
- **Audit:** All data access logged + tamper-evident storage
