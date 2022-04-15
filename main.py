import boto3
import pandas as pd
import redshift_connector


from datetime import datetime

# Declare valiables
date = str(datetime.now())
bucket = 'mibucketredshift-ac'
courses_file = 'course_completes.csv'
AWS_SERVER_PUBLIC_KEY = 'AKIAXMQDSWTQVRRW5I46'
AWS_SERVER_SECRET_KEY = '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'


def connect_to_db():
    try:
        print(date + ' - Connecting to Redshift...')
        con = redshift_connector.connect(  host='redshift-cluster.cjdkillol2ft.us-east-1.redshift.amazonaws.com',
                                            port=5439,
                                            database='dev',
                                            user='user_platzi',
                                            password='Platzi123' )
        print(date + ' - Connected to Redshift...')
        print(str(con))
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM public.category")
            result: tuple = cursor.fetchall()
            print(result)
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))



def extract_from_s3():
    try:
        print(date + ' - Connecting to S3...')
        s3 = boto3.client('s3', aws_access_key_id= AWS_SERVER_PUBLIC_KEY, aws_secret_access_key= AWS_SERVER_SECRET_KEY)
        # s3_resource = boto3.resource('s3', aws_access_key_id= AWS_SERVER_PUBLIC_KEY, aws_secret_access_key= AWS_SERVER_SECRET_KEY)
        print(date + ' - Connection established!')
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))

    try:
        print(date + ' - Validating files existence')
        obj_courses = s3.get_object(Bucket = bucket, Key = courses_file)
        # obj_site = s3.get_object(Bucket = bucket, Key = result_file_site)
        print(date + ' - All files were found!')
    except Exception as e:
        print(date + ' - Validation has an error: ' + str(e))

    try:
        print(date + ' - Generating dataframes')
        df_courses = pd.read_csv(obj_courses['Body'], delimiter=';')
        # df_site = pd.read_csv(obj_site['Body'], delimiter='|')
        print(date + ' - Dataframes generated successfully!')
        print(df_courses)
    except Exception as e:
        print(date + ' - Dataframe generation has an error: ' + str(e))


def load_to_stg():
    pass



def run():
    pass



if __name__ == '__main__':
    connect_to_db()


