"""
Code 4.5: Model Checksum and Integrity Verification Script
Defending Tomorrow - Chapter 4: Secure Model Development

Verifies model integrity before deployment using cryptographic hashing.
"""

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Dict, Optional

def calculate_file_hash(filepath: str, algorithm: str = "sha256") -> str:
    """Calculate hash of a file."""
    hash_func = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def load_manifest(manifest_path: str) -> Dict:
    """Load expected hashes from manifest file."""
    with open(manifest_path, 'r') as f:
        return json.load(f)

def create_manifest(model_path: str, output_path: str, metadata: Optional[Dict] = None):
    """Create a checksum manifest for a model."""
    manifest = {
        "model_file": os.path.basename(model_path),
        "algorithm": "sha256",
        "hash": calculate_file_hash(model_path),
        "size_bytes": os.path.getsize(model_path),
        "timestamp": str(Path(model_path).stat().st_mtime)
    }
    if metadata:
        manifest["metadata"] = metadata
    
    with open(output_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"[✓] Manifest created: {output_path}")
    return manifest

def verify_model(model_path: str, manifest_path: str) -> bool:
    """Verify model against manifest."""
    if not os.path.exists(manifest_path):
        print(f"[!] Manifest not found: {manifest_path}")
        return False
    
    expected = load_manifest(manifest_path)
    actual_hash = calculate_file_hash(model_path)
    
    if actual_hash == expected["hash"]:
        print(f"[✓] Verification PASSED: {model_path}")
        print(f"    Hash matches: {actual_hash[:16]}...")
        return True
    else:
        print(f"[✗] Verification FAILED: {model_path}")
        print(f"    Expected: {expected['hash'][:16]}...")
        print(f"    Actual:   {actual_hash[:16]}...")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Model integrity verification")
    parser.add_argument("--create", help="Create manifest for model file")
    parser.add_argument("--verify", help="Verify model against manifest")
    parser.add_argument("--manifest", help="Path to manifest file")
    parser.add_argument("--metadata", help="JSON metadata for manifest")
    
    args = parser.parse_args()
    
    if args.create:
        manifest_path = args.manifest or f"{args.create}.manifest.json"
        metadata = json.loads(args.metadata) if args.metadata else None
        create_manifest(args.create, manifest_path, metadata)
    
    elif args.verify and args.manifest:
        success = verify_model(args.verify, args.manifest)
        sys.exit(0 if success else 1)
    
    else:
        print("""
Usage:
  # Create manifest
  python model_checksum.py --create model.pth --manifest model.manifest.json
  
  # Verify model
  python model_checksum.py --verify model.pth --manifest model.manifest.json
  
  # In CI/CD pipeline
  python model_checksum.py --verify model.pth --manifest expected.json || exit 1
        """)
