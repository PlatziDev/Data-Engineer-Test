import boto3
import pandas as pd
import redshift_connector
import sqlalchemy

from datetime import datetime


# Declare valiables
date = str(datetime.now())


def connect_to_db():
    try:
        print(date + ' - Connecting to Redshift...')
        con = redshift_connector.connect(  host='redshift-cluster.cjdkillol2ft.us-east-1.redshift.amazonaws.com',
                                           port=5439,
                                           database='platzi',
                                           user='user_platzi',
                                           password='Platzi123' )
        print(date + ' - Connected to Redshift...')
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM dwh.category")
            result: tuple = cursor.fetchall()
            print(result)
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))



def extract():
    bucket = 'mibucketredshift-ac'
    courses_file = 'courses_events.csv'
    subscriptions_file = 'subscriptions_events.csv'
    AWS_SERVER_dwh_KEY = 'AKIAXMQDSWTQVRRW5I46'
    AWS_SERVER_SECRET_KEY = '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'
    try:
        print(date + ' - Connecting to S3...')
        s3 = boto3.client('s3', aws_access_key_id= AWS_SERVER_dwh_KEY, aws_secret_access_key= AWS_SERVER_SECRET_KEY)
        print(date + ' - Connection established!')
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))

    try:
        print(date + ' - Validating files existence')
        obj_courses = s3.get_object(Bucket = bucket, Key = courses_file)
        # obj_subscriptions = s3.get_object(Bucket = bucket, Key = subscriptions_file)
        print(date + ' - All files were found!')
    except Exception as e:
        print(date + ' - Validation has an error: ' + str(e))

    try:
        print(date + ' - Generating dataframes')
        df_courses = pd.read_csv(obj_courses['Body'], delimiter=';',header = 0, names=['id_event', 'first_name', 'last_name', 'email', 'phone', 'class', 'type_event', 'date_event','time'])
        # df_subscriptions = pd.read_csv(obj_subscriptions['Body'], delimiter=';',header = 0, names=['id_event', 'first_name', 'last_name', 'email', 'phone', 'class', 'type_event', 'date_event','time'])
        print(date + ' - Dataframes generated successfully!')
    except Exception as e:
        print(date + ' - Dataframe generation has an error: ' + str(e))

    return df_courses #, df_subscriptions


def transform(df_courses):
    try:
        print(date + ' - Cleaning data')

        # Students Dimention
        df_dimStudents = df_courses.loc[:,['first_name','last_name','email','phone']].drop_duplicates(subset=['first_name','last_name','email','phone'])
        df_dimStudents = df_dimStudents.replace( '-', '', regex=True)

        # Class Dimention
        df_dimClass = df_courses.loc[:,['class']].drop_duplicates(subset=['class'])
        df_dimClass = df_dimClass.replace( '-', '', regex=True)

        print(date + ' - Data has been cleaned!')
    except Exception as e:
        print(date + ' - Error cleaning data: ' + str(e))

    return df_dimStudents,df_dimClass

# def test():
def load(df_clean):
    try:
        print(date + ' - Connecting to Redshift...')
        con = redshift_connector.connect(  host='redshift-cluster.cjdkillol2ft.us-east-1.redshift.amazonaws.com',
                                           port=5439,
                                           database='platzi',
                                           user='user_platzi',
                                           password='Platzi123' )
        print(date + ' - Connected to Redshift!')
        with con.cursor() as cursor:
            print(date + ' - Inserting dim_Students...')
            cursor.execute("DELETE FROM dwh.dim_Students")
            cursor.executemany("INSERT INTO dwh.dim_Students (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)", df_clean.values.tolist())
            con.commit()
            print(date + ' - Inserted dim_Students!')
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))



def main():
    # test()
    df_extract = extract()
    df_clean = transform(df_extract)
    print(df_clean)
    # load(df_clean)


if __name__ == '__main__':
    main()


