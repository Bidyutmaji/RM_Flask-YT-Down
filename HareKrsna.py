import psycopg2

conn = psycopg2.connect(database="dic_live",
                        host="dim-database.cizy3y0o3xp1.ap-south-1.rds.amazonaws.com",
                        user="postgresuser",
                        password="rT6yb%ffgTTvvhf67",
                        port="5432")

cursor = conn.cursor()