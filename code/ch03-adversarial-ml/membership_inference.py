"""
Code 3.2: Basic Membership Inference Attack Demo
Defending Tomorrow - Chapter 3: Adversarial Machine Learning

This demo shows how an attacker can determine if a specific data record
was used to train a target model, using only API access.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_target_model(X_train, y_train):
    """Train the model we will attack."""
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    return model

def membership_inference_attack(model, data_points, labels):
    """
    Simple attack based on prediction confidence.
    Member data often has higher confidence than non-member data.
    """
    confidences = model.predict_proba(data_points)
    max_confidences = np.max(confidences, axis=1)
    
    # Simple threshold attack
    threshold = np.percentile(max_confidences, 70)
    predictions = max_confidences > threshold
    return predictions, max_confidences

def evaluate_attack(attack_predictions, true_membership):
    """Calculate attack accuracy."""
    accuracy = np.mean(attack_predictions == true_membership)
    return accuracy

if __name__ == "__main__":
    print("=== Membership Inference Attack Demo ===\n")
    
    # Generate synthetic dataset
    X, y = make_classification(n_samples=2000, n_features=20, random_state=42)
    
    # Split into training (member) and test (non-member) sets
    X_member, X_nonmember, y_member, y_nonmember = train_test_split(
        X, y, test_size=0.5, random_state=42
    )
    
    # Train target model on member data
    model = train_target_model(X_member, y_member)
    print(f"Target model accuracy: {accuracy_score(y_member, model.predict(X_member)):.2f}\n")
    
    # Prepare attack data
    attack_data = np.vstack([X_member[:100], X_nonmember[:100]])
    true_membership = np.array([1]*100 + [0]*100)  # 1=member, 0=non-member
    
    # Launch attack
    attack_preds, confidences = membership_inference_attack(model, attack_data, None)
    attack_acc = evaluate_attack(attack_preds, true_membership)
    
    print(f"Attack accuracy: {attack_acc:.2f}")
    print(f"Member avg confidence: {np.mean(confidences[:100]):.3f}")
    print(f"Non-member avg confidence: {np.mean(confidences[100:]):.3f}")
    
    if attack_acc > 0.7:
        print("\n[!] Attack successful: model leaks membership information!")
    else:
        print("\n[+] Attack failed: model appears resistant.")
