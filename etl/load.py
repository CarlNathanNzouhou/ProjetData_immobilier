import duckdb

# create the connexion to a database (our database is file that we called real_estate.db)
con = duckdb.connect(database = "data/real_estate.db", read_only = False)

def load_data(estate_df, table_name):
    """
        This function lood data in duckdb database.
        :param: estate_df str is dataframe from csv file, table_name str is name of table
    """
    con.execute(f"CREATE TABLE IF NOT EXISTS '{table_name}' AS SELECT * FROM estate_df ")

    print("Data is load correctly")
    

