# Projet Data Immobilier

Ce projet est une application de tableau de bord pour l'analyse des données immobilières en France. Il utilise Streamlit pour l'interface utilisateur et DuckDB pour la base de données.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt sur votre machine locale :

    ```sh
    git clone https://github.com/votre-utilisateur/projet-data-immobilier.git
    cd projet-data-immobilier
    ```

2. Créez un environnement virtuel et activez-le (Facultatif) :

    ```sh
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances requises :

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Assurez-vous que les fichiers de données nécessaires sont présents dans le dossier `data/` :

- `departements-france.csv` : [Télécharger ici](https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254)
- `ValeursFoncieres-2023.txt` : [Télécharger ici](https://www.data.gouv.fr/fr/datasets/r/dd516f7a-91bb-4cad-a63c-4b55cd457f4c)

## Exécution

Pour démarrer l'application Streamlit, exécutez la commande suivante :

```sh
python -m streamlit run apps.py
```


## Pipeline ETL

Le projet inclut également un pipeline ETL pour extraire, transformer et charger les données dans la base de données DuckDB. Pour exécuter le pipeline ETL, utilisez la commande suivante :

```sh
python pipeline.py
```

## Structure du Projet

- `apps.py` : Fichier principal de l'application Streamlit.
- `config.yaml` : Fichier de configuration pour le pipeline ETL.
- `etl/` : Dossier contenant les scripts ETL (`extract.py`, `transform.py`, `load.py`).
- `workflow/` : Dossier contenant des scripts supplémentaires pour la manipulation des données.
- `data/` : Dossier contenant les fichiers de données.
- `database/` : Dossier contenant la base de données DuckDB.
- `requirements.txt` : Liste des dépendances Python nécessaires pour le projet.

## Auteurs

- Elisabeth NOKAM
- Carl NZOUHOU

