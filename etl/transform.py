# Import the module
import pandas as pd

col_rename = {"no disposition": "no_disposition", "date mutation": "date_mutation", "nature mutation": "nature_mutation", 
              "valeur fonciere": "valeur_fonciere", "code voie": "code_voie", "code postal": "code_postal", 
              "code departement": "code_departement", "code commune": "code_commune", "nombre de lots": "nombre_de_lots", 
              "code type local": "code_type_local", "type local": "type_local", "surface reelle bati": "surface_reelle_bati", 
              "nombre pieces principales": "nombre_pieces"}

col_drop = ['No Volume', '1er lot', 'Surface Carrez du 1er lot', '2eme lot', 
            'Surface Carrez du 2eme lot', '3eme lot', 'Surface Carrez du 3eme lot', 
            '4eme lot', 'Surface Carrez du 4eme lot', '5eme lot', 'Surface Carrez du 5eme lot']

def transform_data(estate_df : object):
    """
        This function transform data which have extract.
        :param reat_estate: extracted data file in csv format
        :outpout: data file transformed  
    """

    # delete columns with more 90% missing values
    estate_df = estate_df.drop(col_drop, axis = 1)

    # convert columns to appropriate data types
    estate_df['Date mutation'] = pd.to_datetime(estate_df['Date mutation'], format ='%d/%m/%Y')
    estate_df['Valeur fonciere'] = estate_df['Valeur fonciere'].str.replace(',', '.')
    estate_df['Valeur fonciere'] = estate_df['Valeur fonciere'].astype(float)
    estate_df.columns = estate_df.columns.str.lower()

    # rename columns
    estate_df = estate_df.rename(columns = col_rename)

    print("The process is transformation is finish")

    return estate_df 
