from db.create import insert_tables, insert_er_data
from etl import *

if __name__ == "__main__":
    insert_tables()
    insert_er_data()
    
    #Get data from relational model and insert it into the star model
    print('Processing data')
    payment_date_dim()
    subscription_dim()
    student_dim()
    sales_dim()

    print('\nAll data was inserted into the Star model.\n')
