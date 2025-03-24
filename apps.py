import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(page_title="Dashboard Imo France", page_icon=":bar_chart:", layout="wide")

st.title("Dashboard Immobilier en France")

# Chargement des données
df_departements = pd.read_csv("data/departements-france.csv")
df_valeurs = pd.read_csv("data/ValeursFoncieres-2023.txt", sep='|', low_memory=False)

# Vérification des colonnes avant la fusion
st.write("Colonnes de df_departements:", df_departements.columns)
st.write("Colonnes de df_valeurs:", df_valeurs.columns)

# Fusion des données sur le champ commun (par exemple, 'code_departement')
df = pd.merge(df_valeurs, df_departements, left_on='Code departement', right_on='code_departement', how='left')

# Vérification des colonnes après la fusion
st.write("Colonnes après fusion:", df.columns)

# Conversion des dates
df['date'] = pd.to_datetime(df['Date mutation'], errors='coerce')

# Conversion de la colonne 'Valeur fonciere' en numérique
df['Valeur fonciere'] = pd.to_numeric(df['Valeur fonciere'].str.replace(',', '.'), errors='coerce')

# Suppression des lignes avec des valeurs manquantes dans 'Valeur fonciere'
df = df.dropna(subset=['Valeur fonciere'])

# Filtres interactifs
region = st.selectbox("Sélectionnez une région", options=["Toutes"] + df['nom_region'].unique().tolist())
departement = st.selectbox("Sélectionnez un département", options=["Tous"] + df['nom_departement'].unique().tolist())
type_local = st.selectbox("Sélectionnez un type de local", options=["Tous"] + df['Type local'].unique().tolist())

# Filtrage des données
if region != "Toutes":
    df = df[df['nom_region'] == region]
if departement != "Tous":
    df = df[df['nom_departement'] == departement]
if type_local != "Tous":
    df = df[df['Type local'] == type_local]

# Calcul des statistiques
total_ventes = df['Valeur fonciere'].sum()
montant_moyen = df['Valeur fonciere'].mean()
ventes_par_type = df.groupby('Type local')['Valeur fonciere'].mean().reset_index()
ventes_par_mois = df.groupby(df['date'].dt.to_period('M')).size().reset_index(name='count')
ventes_par_mois['date'] = ventes_par_mois['date'].astype(str)
montant_moyen_trimestre = df.groupby(df['date'].dt.to_period('Q'))['Valeur fonciere'].mean().reset_index(name='mean')
montant_moyen_trimestre['date'] = montant_moyen_trimestre['date'].astype(str)

# Vérification de l'existence de la colonne 'nom_departement'
if 'nom_departement' in df.columns:
    prix_moyen_departement = df.groupby('nom_departement')['Valeur fonciere'].mean().reset_index(name='mean')
else:
    st.write("La colonne 'nom_departement' n'existe pas dans le DataFrame fusionné.")
    prix_moyen_departement = pd.DataFrame()

# Affichage des statistiques
st.write(f"Total des ventes: {total_ventes}")
st.write(f"Montant moyen: {montant_moyen}")

st.subheader("Montant moyen par type de local")
st.dataframe(ventes_par_type)

st.subheader("Évolution du nombre de ventes par mois")
fig1 = px.line(ventes_par_mois, x='date', y='count', title="Évolution du nombre de ventes par mois")
st.plotly_chart(fig1)

st.subheader("Montant moyen par trimestre")
fig2 = px.bar(montant_moyen_trimestre, x='date', y='mean', title="Montant moyen par trimestre")
st.plotly_chart(fig2)

if not prix_moyen_departement.empty:
    st.subheader("Prix moyen par département")
    fig3 = px.bar(prix_moyen_departement, x='nom_departement', y='mean', title="Prix moyen par département")
    st.plotly_chart(fig3)

# Statistiques supplémentaires à partir de departements-france.csv
st.subheader("Statistiques supplémentaires des départements")

# Nombre total de départements
total_departements = df_departements.shape[0]
st.write(f"Nombre total de départements: {total_departements}")

# Nombre de départements par région
departements_par_region = df_departements['nom_region'].value_counts()
st.subheader("Nombre de départements par région")
st.dataframe(departements_par_region)

# Liste des départements par région
departements_par_region_liste = df_departements.groupby('nom_region')['nom_departement'].apply(list)
st.subheader("Liste des départements par région")
st.dataframe(departements_par_region_liste)

# Recherche de département par code
code_departement = st.text_input("Entrez un code de département pour rechercher ses informations", "")
if code_departement:
    departement_info = df_departements[df_departements['code_departement'] == code_departement]
    st.write(f"Informations pour le département {code_departement}:")
    st.dataframe(departement_info)

# Recherche de département par nom
nom_departement = st.text_input("Entrez un nom de département pour rechercher ses informations", "")
if nom_departement:
    departement_info = df_departements[df_departements['nom_departement'] == nom_departement]
    st.write(f"Informations pour le département {nom_departement}:")
    st.dataframe(departement_info)

# Nombre total de régions
total_regions = df_departements['nom_region'].nunique()
st.write(f"Nombre total de régions: {total_regions}")

# Liste des régions
liste_regions = df_departements[['code_region', 'nom_region']].drop_duplicates().sort_values('code_region')
st.subheader("Liste des régions")
st.dataframe(liste_regions)

# Prix moyen par type de département
prix_moyen_par_departement = df.groupby('nom_departement')['Valeur fonciere'].mean().reset_index(name='prix_moyen')
st.subheader("Prix moyen par type de département")
st.dataframe(prix_moyen_par_departement)

# Prix moyen par région
prix_moyen_par_region = df.groupby('nom_region')['Valeur fonciere'].mean().reset_index(name='prix_moyen')
st.subheader("Prix moyen par région")
st.dataframe(prix_moyen_par_region)

# Carte interactive des prix moyens par département
st.subheader("Carte des prix moyens par département")
fig4 = px.choropleth(df, geojson="https://france-geojson.gregoiredavid.fr/repo/departements.geojson", 
                     locations='code_departement', featureidkey="properties.code", color='Valeur fonciere',
                     hover_name='nom_departement', title="Prix moyens par département")
fig4.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig4)

# Onglets
tab1, tab2 = st.tabs(["Cat", "Dog"])

with tab1:
    input_text = st.text_area(label="Entrez votre input")
    st.write(input_text)

    if df is not None:  # Vérifie que df existe avant de l'afficher
        st.dataframe(df.head(10))  # Afficher seulement les 10 premières lignes

with tab2:
    input_v = st.text_area(label="Entrez votre code")
    st.write(input_v)

    if df is not None:
        st.dataframe(df.head(10))  # Afficher seulement les 10 premières lignes
