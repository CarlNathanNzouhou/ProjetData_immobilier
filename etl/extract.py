# Import the module

import pandas as pd

def extraction_data(filepath: object, select_col: list) -> object:
    """
        This fonction extract data of real estate and take tree parameters
        : param filepath: str file txt
        : output: data extracted in csv format
    """
    try:
        estate_df = pd.read_csv(filepath, sep = "|", low_memory = False)
        estate_df = estate_df[select_col]

        print(f"Data : {filepath} have extracted correctly.")

    except FileNotFoundError as e:
        print(f"Error, file {filepath} is not found.")

    except Exception as e:
        print(f"Error : {e} during extraction.")

    return estate_df 


def extract_data_dpt(filepath : object):
    """
        This fonction extracte data of France department
        :param filepath : str file in csv data
        :output : data extracted from csv file 
    """
    try:
        dept_df = pd.read_csv(filepath)
        print(f"Data of {filepath} extracted correctly.")
    except Exception as e:
        print(f"Error : {e} during extraction.")

    return dept_df
