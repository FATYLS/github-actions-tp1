# model.py

import random
import json

# Fonction simulant l'évaluation d'un modèle
def evaluate_model():
    """
    Cette fonction simule l'évaluation d'un modèle de machine learning
    et génère des métriques de performance comme l'accuracy, la precision,
    le recall et le F1-score.
    """
    metrics = {
        "accuracy": round(random.uniform(0.85, 0.95), 3),  # Précision du modèle (entre 0.85 et 0.95)
        "precision": round(random.uniform(0.80, 0.98), 3),  # Précision de la classification
        "recall": round(random.uniform(0.80, 0.98), 3),  # Rappel de la classification
        "f1_score": round(random.uniform(0.80, 0.98), 3)  # Score F1 de la classification
    }
    
    # Sauvegarde des métriques dans un fichier JSON
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    
    print(f"Model metrics: {metrics}")  # Affiche les métriques générées
    return metrics  # Retourne les métriques pour une utilisation ultérieure

# Si le script est exécuté directement, lance l'évaluation
if __name__ == "__main__":
    evaluate_model()
