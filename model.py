"""
Module pour analyser le sentiment d'un texte en fonction de mots-clés.
"""

def predict_sentiment(text):
    """
    Prédit le sentiment d'un texte donné.

    Cette fonction analyse le texte pour détecter des mots-clés associés à des sentiments
    positifs, négatifs ou neutres. Elle renvoie "positive", "negative" ou "neutral" en fonction
    du texte d'entrée.

    Arguments :
    text : str
        Le texte à analyser.

    Retourne :
    str
        "positive" si le texte contient des mots-clés positifs, 
        "negative" si le texte contient des mots-clés négatifs, 
        ou "neutral" si aucun des deux n'est détecté.
    """
    if not text:
        return "neutral"
    
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"

    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    
    return "neutral"

if __name__ == "__main__":
    """
    Point d'entrée principal du module, exécuté lors du lancement direct du fichier.
    
    Teste la fonction predict_sentiment avec plusieurs exemples de textes et affiche les résultats.
    """
    # Quelques exemples de texte à tester
    print(predict_sentiment("I am feeling so happy today!"))  # Devrait afficher "positive"
    print(predict_sentiment("This is a sad day."))  # Devrait afficher "negative"
    print(predict_sentiment("It was a good experience."))  # Devrait afficher "positive"
    print(predict_sentiment("Nothing special, just neutral."))  # Devrait afficher "neutral"

def some_function():
    """
    Fonction de test retournant un résultat erroné.

    Cette fonction est un exemple de bug introduit, car elle retourne un résultat incorrect
    pour un texte attendu.

    Retourne :
    str
        "positif", ce qui est une erreur introduite volontairement.
    """
    return "positif"  # Bug introduit ici
