import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données (remplacer par le chargement réel dans une appli Streamlit)
def load_data():
    file_path = "sergic_verbatim_data.csv"  # Remplacer par le vrai fichier
    df = pd.read_csv(file_path, delimiter=";")
    df.columns = ["Période", "Degré de satisfaction", "Commentaire", "Codage positif", "Codage négatif"]
    return df

df = load_data()

st.set_page_config(page_title="Analyse Satisfaction Client - SERGIC", layout="wide")

st.title("Analyse de la Satisfaction Client - SERGIC")

# Onglets pour l'analyse
tabs = st.tabs(["Vue Globale", "Par Thématique", "Problèmes Identifiés", "Plan d’Action"])

# Vue Globale
with tabs[0]:
    st.header("Vue Globale de la Satisfaction")
    
    satisfaction_counts = df["Degré de satisfaction"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(satisfaction_counts, labels=satisfaction_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    
    st.write("Détail des verbatims par période :")
    st.dataframe(df.groupby("Période")["Degré de satisfaction"].value_counts().unstack())

# Analyse par Thématique
with tabs[1]:
    st.header("Analyse par Thématique")
    themes = df["Codage positif"].dropna().unique()
    selected_theme = st.selectbox("Choisissez une thématique :", themes)
    
    st.write(df[df["Codage positif"] == selected_theme][["Commentaire", "Période"]])

# Problèmes Identifiés
with tabs[2]:
    st.header("Problèmes Identifiés")
    issues = df["Codage négatif"].dropna().value_counts()
    st.bar_chart(issues)
    
    st.write("Exemples de verbatims négatifs :")
    st.dataframe(df[df["Codage négatif"].notna()][["Commentaire", "Codage négatif"]])

# Plan d’Action
with tabs[3]:
    st.header("Plan d’Action")
    
    recommendations = {
        "Manque de réactivité": "Mettre en place un suivi plus rigoureux des demandes clients.",
        "Problèmes techniques": "Renforcer l'équipe technique et améliorer la maintenance.",
        "Communication insuffisante": "Envoyer des mises à jour régulières sur les interventions."
    }
    
    for issue, action in recommendations.items():
        st.subheader(issue)
        st.write(action)
    
    st.write("Suggestions complémentaires :")
    user_suggestion = st.text_area("Ajoutez votre suggestion :")
    if st.button("Soumettre"):
        st.write("Merci pour votre contribution !")
