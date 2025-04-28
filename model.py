def predict_sentiment(text):
    if not text:
        return "neutral"
    
    if "happy" in text.lower() or "good" in text.lower():
        return "positif"
   

    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    
    return "neutral"

if __name__ == "__main__":
    # Quelques exemples de texte à tester
    print(predict_sentiment("I am feeling so happy today!"))  # Devrait afficher "positive"
    print(predict_sentiment("This is a sad day."))  # Devrait afficher "negative"
    print(predict_sentiment("It was a good experience."))  # Devrait afficher "positive"
    print(predict_sentiment("Nothing special, just neutral."))  # Devrait afficher "neutral"
def some_function():
    return "positif"  # Bug introduit ici
