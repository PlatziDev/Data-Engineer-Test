import psycopg2 as pg2
import pandas as pd

def connect():
    conn = pg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="dataplatzi"
            )
    return conn

def get_db_data(query):
    """ Run query and return a Dataframe """
    try:
        conn = connect()
        cur = conn.cursor() 

        result = pd.read_sql(query, conn)

        conn.close()

        return result

    except (Exception, pg2.DatabaseError) as error:
        print(error)

def insert_data(query):
    """ Insert data into DB """
    try:
        conn = connect()
        cur = conn.cursor() 

        cur.execute(query)
        conn.commit()

        conn.close()

    except (Exception, pg2.DatabaseError) as error:
        print(error)