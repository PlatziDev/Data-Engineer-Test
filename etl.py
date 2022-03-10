import pandas as pd
import psycopg2 as pg2
from psycopg2 import Error
import warnings
#Ignore pandas future warning
warnings.simplefilter(action='ignore', category=FutureWarning)

from db.conn import get_db_data, insert_data
from db.queries import fact_sales_query, dim_payment_date_query, dim_student_query, dim_subscription_query

def payment_date_dim():
    payment_df = get_db_data(dim_payment_date_query)

    #Extract Day, Week, Month and year from date
    payment_df['day'] = pd.to_datetime(payment_df['payment_date']).dt.day
    payment_df['week'] = pd.to_datetime(payment_df['payment_date']).dt.week
    payment_df['month'] = pd.to_datetime(payment_df['payment_date']).dt.month
    payment_df['year'] = pd.to_datetime(payment_df['payment_date']).dt.year

    payment_df['payment_date'] = pd.to_datetime(payment_df['payment_date'])

    #Dataframe to query, using this way because we are using psycopg2
    #Iterate through the dataframe and insert the data into star model
    for index, row in payment_df.iterrows():
        query = """INSERT INTO payment_date_dim (payment_id, date, day, week, month, year) 
                    VALUES (%s,'%s'::date,%s,%s,%s,%s)""" % (row['payment_id'], row['payment_date'],row['day'],row['week'],
                    row['month'],row['year'])
                        
        insert_data(query)

def subscription_dim():
    subs_df = get_db_data(dim_subscription_query)

    for index, row in subs_df.iterrows():
        query = """INSERT INTO subscription_dim (subscription_id, type) 
                    VALUES (%s,'%s')""" % (row['subscription_id'], row['type'])
                        
        insert_data(query)
    
def student_dim():
    student_df = get_db_data(dim_student_query)

    for index, row in student_df.iterrows():
        query = """ INSERT INTO student_dim (student_id, first_name, last_name, user_name, country, gender, status) 
                    VALUES (%s,'%s','%s','%s','%s','%s','%s')""" % (row['student_id'], row['first_name'], row['last_name'], 
                    row['user_name'], row['country'], row['gender'], row['status'])
        
        insert_data(query)

def sales_dim():
    sales_df = get_db_data(fact_sales_query)

    for index, row in sales_df.iterrows():
        query = """ INSERT INTO sales_fact (payment_ammount, currency, payment_method, student_id, subscription_id, payment_id) 
                    VALUES (%s,'%s','%s',%s,%s,%s)""" % (row['payment_ammount'],row['currency'],row['payment_method'],
                    row['student_id'],row['subscription_id'],row['payment_id'])
        
        insert_data(query)
