import json
import random

def evaluate_model():
    # Simulation d'évaluation avec accuracy pouvant être inférieure à 0.9
    metrics = {
        "accuracy": round(random.uniform(0.85, 0.95), 3),  # Plage modifiée
        "precision": round(random.uniform(0.80, 0.98), 3),
        "recall": round(random.uniform(0.80, 0.98), 3),
        "f1_score": round(random.uniform(0.80, 0.98), 3)
    }
    
    # Sauvegarder les résultats dans un fichier JSON
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    
    print(f"Model metrics: {metrics}")
    return metrics

if __name__ == "__main__":
    evaluate_model()
