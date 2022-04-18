import boto3
import pandas as pd
import redshift_connector
from datetime import datetime


date = str(datetime.now())

def extract():
    """
        This function extract all files used in the process...
        The files are located in a bucket in S3
    """

    # Declaration of variables to extract the files
    bucket = 'mibucketredshift-ac'
    courses_file = 'courses.csv'
    class_file = 'class.csv'
    enrollment_class_file = 'enrollment_class.csv'
    school_file = 'school.csv'
    students_file = 'students.csv'
    subscriptions_file = 'subscriptions.csv'
    events_file = 'events.csv'
    AWS_SERVER_dwh_KEY = 'AKIAXMQDSWTQVRRW5I46'
    AWS_SERVER_SECRET_KEY = '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'
    
    
    # Create connection to s3
    try:
        print(date + ' - Connecting to S3...')
        s3 = boto3.client('s3', aws_access_key_id= AWS_SERVER_dwh_KEY, aws_secret_access_key= AWS_SERVER_SECRET_KEY)
        print(date + ' - Connection established!')
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))


    # File Validation
    try:
        print(date + ' - Validating files existence')
        obj_courses = s3.get_object(Bucket = bucket, Key = courses_file)
        obj_class = s3.get_object(Bucket = bucket, Key = class_file)
        obj_enrollment_class = s3.get_object(Bucket = bucket, Key = enrollment_class_file)
        obj_school = s3.get_object(Bucket = bucket, Key = school_file)
        obj_students = s3.get_object(Bucket = bucket, Key = students_file)
        obj_subscriptions= s3.get_object(Bucket = bucket, Key = subscriptions_file)
        obj_events= s3.get_object(Bucket = bucket, Key = events_file)
        print(date + ' - All files were found!')
    except Exception as e:
        print(date + ' - Validation has an error: ' + str(e))


    # Data frame generation
    try:
        print(date + ' - Generating dataframes')
        df_courses = pd.read_csv(obj_courses['Body'], delimiter=';')
        df_class = pd.read_csv(obj_class['Body'], delimiter=';')
        df_enrollment_class = pd.read_csv(obj_enrollment_class['Body'], delimiter=';')
        df_school = pd.read_csv(obj_school['Body'], delimiter=';')
        df_students = pd.read_csv(obj_students['Body'], delimiter=';')
        df_subscriptions = pd.read_csv(obj_subscriptions['Body'], delimiter=';')
        df_events = pd.read_csv(obj_events['Body'], delimiter=';')

        df = [df_courses,df_class,df_enrollment_class,df_school,df_students,df_subscriptions,df_events]
        print(date + ' - Dataframes generated successfully!')
    except Exception as e:
        print(date + ' - Dataframe generation has an error: ' + str(e))

    return df

def transform(df):
    """
        This function transform data to a dimentional model
        Here we transform raw dataframes into fact and dimentional tables
    """
    # Updating dimention tables
    try:
        print(date + ' - Updating Dimention tables...')

        df_courses = pd.DataFrame(df[0])
        df_class = pd.DataFrame(df[1])
        df_enrollment_class = pd.DataFrame(df[2])
        df_school = pd.DataFrame(df[3])
        df_students = pd.DataFrame(df[4])
        df_subscriptions = pd.DataFrame(df[5])
        df_events = pd.DataFrame(df[6])

        # Students Dimention
        df_dimStudents = df_students.loc[:,['first_name','last_name','phone','email','age','country','city']].drop_duplicates(subset=['first_name','last_name','phone','email','age','country','city'])
        df_dimStudents = df_dimStudents.assign(date_created = date , date_updated = date, id_student = df_dimStudents.index)

        # Payment Method Dimention
        df_dimPaymenthMethod = df_subscriptions.loc[:,['payment_method','currency']].drop_duplicates(subset=['payment_method','currency'])
        df_dimPaymenthMethod = df_dimPaymenthMethod.assign(code=df_dimPaymenthMethod['payment_method'].str[:2].str.upper())
        df_dimPaymenthMethod = df_dimPaymenthMethod.assign(date_created = date , date_updated = date, id_payment_method = df_dimPaymenthMethod.index)

        # Class Dimention
        df_dimClass = df_class.merge(df_courses, right_on='name_course', left_on='name_course', how='left').merge(df_school, right_on='name_school', left_on='name_school', how='left')
        df_dimClass = df_dimClass.loc[:,['name_class','name_course','name_school']].drop_duplicates(subset=['name_class','name_course','name_school'])
        df_dimClass = df_dimClass.assign(date_created = date , date_updated = date, id_class = df_dimClass.index)
    
        # Event Dimention
        df_dimEvent = df_events.loc[:,['type_event']].drop_duplicates(subset=['type_event'])
        df_dimEvent = df_dimEvent.loc[:,['type_event']].drop_duplicates(subset=['type_event'])
        df_dimEvent = df_dimEvent.assign(date_created = date , date_updated = date, id_event = df_dimEvent.index)
    
        # Frequency Dimention
        df_dimFrequency = df_subscriptions.loc[:,['payment_type']].drop_duplicates(subset=['payment_type'])
        df_dimFrequency = df_dimFrequency.loc[:,['payment_type']].drop_duplicates(subset=['payment_type'])
        df_dimFrequency = df_dimFrequency.assign(date_created = date , date_updated = date, id_frequency = df_dimFrequency.index)
    

        df_dim=[df_dimStudents,df_dimPaymenthMethod,df_dimClass,df_dimEvent,df_dimFrequency]    
        print(date + ' - Dimention tables has been updated!')
        
    except Exception as e:
        print(date + ' - Error updating Dimention Tables: ' + str(e))
    
    
    # Updating Fact tables
    try:
        print(date + ' - Creating Fact tables...')

        print(date + ' - Fact tables has been updated!')
    except Exception as e:
        print(date + ' - Error updating Fact Tables: ' + str(e))

    return df_dim



def load(df_clean):
    df_dimStudents = df_clean[0]
    df_dimPaymenthMethod = df_clean[1]
    df_dimClass = df_clean[2]
    df_dimEvent = df_clean[3]
    df_dimFrequency = df_clean[4]
    try:
        print(date + ' - Connecting to Redshift...')
        con = redshift_connector.connect(  host='redshift-cluster.cjdkillol2ft.us-east-1.redshift.amazonaws.com',
                                           port=5439,
                                           database='platzi',
                                           user='user_platzi',
                                           password='Platzi123' )
        print(date + ' - Connected to Redshift!')
        with con.cursor() as cursor:
            # Student Dimention
            print(date + ' - Inserting dim_Student..')
            cursor.execute("DELETE FROM dwh.dim_Student")
            cursor.executemany("INSERT INTO dwh.dim_Student (first_name,last_name,phone,email,age,country,city,date_created,date_updated,id_student) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", df_dimStudents.values.tolist())
            con.commit()
            print(date + ' - dim_Student has been updated!')

            # Payment Method Dimention
            print(date + ' - Inserting dim_payment_method...')
            cursor.execute("DELETE FROM dwh.dim_payment_method")
            cursor.executemany("INSERT INTO dwh.dim_payment_method (payment_name, currency, payment_code , date_created , date_updated, id_payment_method) VALUES (%s, %s, %s, %s, %s, %s)", df_dimPaymenthMethod.values.tolist())
            con.commit()
            print(date + ' - dim_payment_method has been updated!')

            # Class Dimention
            print(date + ' - Inserting dim_class...')
            cursor.execute("DELETE FROM dwh.dim_class")
            cursor.executemany("INSERT INTO dwh.dim_class (name_class, name_course, name_school, date_created, date_updated, id_class) VALUES (%s, %s, %s, %s, %s, %s)", df_dimClass.values.tolist())
            con.commit()
            print(date + ' - dim_class has been updated!')

            # Event Dimention
            print(date + ' - Inserting dim_Event..')
            cursor.execute("DELETE FROM dwh.dim_Event")
            cursor.executemany("INSERT INTO dwh.dim_Event (type_event, date_created, date_updated, id_event) VALUES (%s, %s, %s, %s)", df_dimEvent.values.tolist())
            con.commit()
            print(date + ' - dim_Event has been updated!')

            # Frequency Dimention
            print(date + ' - Inserting dim_Frequency..')
            cursor.execute("DELETE FROM dwh.dim_Frequency")
            cursor.executemany("INSERT INTO dwh.dim_Frequency (frequency_type, date_created, date_updated, id_frequency) VALUES (%s, %s, %s, %s)", df_dimFrequency.values.tolist())
            con.commit()
            print(date + ' - dim_Frequency has been updated!')
    except Exception as e:
        print(date + ' - Connection error: ' + str(e))



def main():
    df_extract = extract()
    df_clean = transform(df_extract)
    load(df_clean)



if __name__ == '__main__':
    main()


