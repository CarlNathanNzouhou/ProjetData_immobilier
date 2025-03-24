import duckdb 
import pandas

con = duckdb.connect(database = "database/real_estate.db", read_only = False)
df_data = con.execute("SELECT * FROM zone_geographique").df()

df_fimo = con.execute("""
                        SELECT 
                            date_mutation,
                            DAYOFWEEK(date_mutation) AS jour_semaine,
                            nature_mutation,
                            valeur_fonciere,
                            code_postal,
                            commune,
                            code_departement,
                            code_commune,
                            type_local,
                            surface_reelle_bati,
                            nombre_pieces
                        FROM immo_france
                      """
                      ).df()

