import psycopg2 as pg2
from psycopg2 import Error
import os

#PostgreSQL connection file
from db.conn import *
#External file that stores the queries
from db.queries import dimension_tables_query, fact_tables_query

def insert_tables():
   
    #Insert dimension tables
    insert_data(dimension_tables_query)
    print('Dimension tables created')

    #Insert Fact tables
    insert_data(fact_tables_query)
    print('Star model created')
        

def insert_er_data():
    try: 
        #Database connection
        conn = connect()
        cur = conn.cursor()

        files = [
            'db/data/student.csv',
            'db/data/subscription_type.csv',
            'db/data/subscription.csv',
            'db/data/payment_method.csv',
            'db/data/payment_currency.csv',
            'db/data/payment.csv',
            'db/data/school.csv',
            'db/data/course.csv',
            'db/data/class.csv',
            'db/data/student_path.csv',
            'db/data/student_progress.csv',
            'db/data/subscription_history.csv'
        ]

        #Iterate through all files
        for file in files:
            filename = os.path.basename(file).split(".")[0]
            with open(file, 'r') as f:
                #Skip the header
                next(f)
                cur.copy_from(f, filename, sep=',')
        
        conn.commit()
        conn.close()
        print('\nAll data was inserted into the relational tables.')
        
    except (Exception, pg2.DatabaseError) as error:
        print(error)
