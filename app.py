from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import streamlit as st

# Charger le tokenizer et le modèle
tokenizer = AutoTokenizer.from_pretrained("ac0hik/Sentiment_Analysis_French")
model = AutoModelForSequenceClassification.from_pretrained("ac0hik/Sentiment_Analysis_French")

# Créer un pipeline d’analyse de sentiments
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Exemple d'utilisation

texte = st.text_area("Entrez un texte pour analyse de sentiment")
if texte:
    resultat = nlp(texte)
    st.write(resultat)

