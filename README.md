# FrSentimentAppAnalyser

# 🇫🇷 Analyse de Sentiment en Français avec Transformers & Streamlit

Cette application permet d’analyser le **sentiment de textes en français** grâce au modèle pré-entraîné <a href="https://huggingface.co/ac0hik/Sentiment_Analysis_French">ac0hik/Sentiment_Analysis_French</a> via une interface simple construite avec **Streamlit**.

## 🚀 Fonctionnalités

- Chargement automatique du modèle depuis Hugging Face
- Interface utilisateur pour l’analyse de texte
- Prédictions : `positive`, `neutral`, `negative`
- Déploiement possible sur Streamlit Cloud, AWS, etc.

## 📦 Installation

```bash
git clone https://github.com/votre-utilisateur/sentiment-fr-app.git
cd sentiment-fr-app

# Créer un environnement virtuel (optionnel)
python -m venv venv
source venv/bin/activate  # sous Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

**requirements.txt :**
```text
streamlit
transformers
torch
```

## ▶️ Utilisation

```bash
streamlit run app.py
```

## 📁 Structure du projet

```
sentiment-fr-app/
├── app.py                 # Application Streamlit
├── requirements.txt       # Dépendances
└── README.md              # Documentation
```

## 🧪 Exemple

```text
texte = st.text_area("Entrez un texte pour analyse de sentiment")
if texte:
    resultat = nlp(texte)
    st.write(resultat)
```

## 🔗 Ressources

- Modèle Hugging Face : [ac0hik/Sentiment_Analysis_French](https://huggingface.co/ac0hik/Sentiment_Analysis_French)
- Transformers : https://huggingface.co/docs/transformers
- Streamlit : https://docs.streamlit.io/
