#
import yaml
from etl.extract import *
from etl.transform import transform_data
from etl.load import load_data


# import pipiline configuration
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

def run_pipeline():
    """
        This function combine all step of ETL
    """
    # step 1 extract data
    df_imo = extraction_data(config_data['real_estate'], config_data['select_col'])
    df_dpt = extract_data_dpt(config_data['france_dept']) 

    # step 2 transform data
    df_imo_t = transform_data(df_imo) 

    # step 3 load data in databese duckdb
    load_data(df_imo_t, 'immo_france')
    load_data(df_dpt, 'zone_geographique')

if __name__ == "__main__":
    run_pipeline()