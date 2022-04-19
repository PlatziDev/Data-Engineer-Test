import boto3
import pandas as pd
import redshift_connector
import warnings
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
        print('\n' + date + ' - Connecting to S3...')
        s3 = boto3.client('s3', aws_access_key_id= AWS_SERVER_dwh_KEY, aws_secret_access_key= AWS_SERVER_SECRET_KEY)
        print(date + ' - Connection established!')
    except Exception as e:
        print(date + ' - Connection ERROR: ' + str(e))


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
        print(date + ' - Validation has an ERROR: ' + str(e))


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
        print(date + ' - Dataframe generation has an ERROR: ' + str(e))

    return df



def transform(df):
    """
        This function transform data to a dimentional model
        Here we transform raw dataframes into fact and dimentional tables
    """
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # Updating dimention tables
    try:
        print('\n' + date + ' - Updating Dimention tables...')

        df_courses = pd.DataFrame(df[0])
        df_class = pd.DataFrame(df[1])
        df_enrollment_class = pd.DataFrame(df[2])
        df_school = pd.DataFrame(df[3])
        df_students = pd.DataFrame(df[4])
        df_subscriptions = pd.DataFrame(df[5])
        df_events = pd.DataFrame(df[6])

        # Students Dimention
        df_dimStudents = df_students.loc[:,['id','first_name','last_name','phone','email','age','country','city']].drop_duplicates(subset=['id','first_name','last_name','phone','email','age','country','city'])
        df_dimStudents = df_dimStudents.assign(date_created = date , date_updated = date, id_student = df_dimStudents.index)

        # Payment Method Dimention
        df_dimPaymenthMethod = df_subscriptions.loc[:,['id','payment_method','currency']].drop_duplicates(subset=['id','payment_method','currency'])
        df_dimPaymenthMethod = df_dimPaymenthMethod.sort_values('id').groupby(['payment_method','currency']).tail(1)
        df_dimPaymenthMethod = df_dimPaymenthMethod.assign(code=df_dimPaymenthMethod['payment_method'].str[:2].str.upper())
        df_dimPaymenthMethod = df_dimPaymenthMethod.assign(date_created = date , date_updated = date, id_payment_method = df_dimPaymenthMethod.index)
        
        # Class Dimention
        df_dimClass = df_class.merge(df_courses, right_on='name_course', left_on='name_course', how='left').merge(df_school, right_on='name_school', left_on='name_school', how='left')
        df_dimClass = df_dimClass.loc[:,['name_class','name_course','name_school']].drop_duplicates(subset=['name_class','name_course','name_school'])
        df_dimClass = df_dimClass.assign(date_created = date , date_updated = date, id_class = df_dimClass.index)
    
        # Event Dimention
        df_dimEvent = df_events.loc[:,['id','type_event','duration']].drop_duplicates(subset=['id','type_event','duration'])
        df_dimEvent = df_dimEvent.sort_values('id').groupby(['type_event','duration']).tail(1)
        df_dimEvent = df_dimEvent.assign(date_created = date , date_updated = date, id_event = df_dimEvent.index)
    
        # Frequency Dimention
        df_dimFrequency = df_subscriptions.loc[:,['id','payment_type','cant_payments']].drop_duplicates(subset=['id','payment_type','cant_payments'])
        df_dimFrequency = df_dimFrequency.sort_values('id').groupby(['payment_type','cant_payments']).tail(1)
        df_dimFrequency = df_dimFrequency.assign(date_created = date , date_updated = date, id_frequency = df_dimFrequency.index)
    
        # Time Dimention
        df_dimTime = pd.DataFrame({"date": pd.date_range('2020-01-01', '2022-12-31')})
        df_dimTime["day"] = df_dimTime.date.dt.day
        df_dimTime["week"] = df_dimTime.date.dt.week
        df_dimTime["month"] = df_dimTime.date.dt.month
        df_dimTime["quarter"] = df_dimTime.date.dt.quarter
        df_dimTime["year"] = df_dimTime.date.dt.year
        df_dimTime.insert(0, 'date_id', (df_dimTime.year.astype(str) + df_dimTime.month.astype(str).str.zfill(2) + df_dimTime.day.astype(str).str.zfill(2)).astype(int))
        df_dimTime = df_dimTime.assign(date_created = date , date_updated = date)

        df_dim=[df_dimStudents,df_dimPaymenthMethod,df_dimClass,df_dimEvent,df_dimFrequency,df_dimTime]
        print(date + ' - Dimention tables has been updated!')
        
    except Exception as e:
        print(date + ' - ERROR updating Dimention Tables: ' + str(e))
    
    
    # Updating Fact tables
    try:
        print('\n' + date + ' - Creating Fact tables...')

        # Fact subscription
        df_subscriptions['id_date']= pd.to_datetime(df_subscriptions['created_at']).dt.strftime('%Y%m%d')
        df_factSubscription = pd.merge(df_subscriptions, df_events, left_on='id_user', right_on='id_user', how = 'left',suffixes=('_subscriptions', '_events')).drop_duplicates()
        df_factSubscription = pd.merge(df_factSubscription, df_dimStudents, left_on='id_user', right_on='id', how = 'left').drop_duplicates()
        df_factSubscription = pd.merge(df_factSubscription, df_dimEvent, left_on=['type_event','duration'], right_on=['type_event','duration'], how = 'left').drop_duplicates()
        df_factSubscription = pd.merge(df_factSubscription, df_dimPaymenthMethod, left_on=['payment_method','currency'], right_on=['payment_method','currency'], how = 'left').drop_duplicates()
        df_factSubscription = pd.merge(df_factSubscription, df_dimFrequency, left_on=['payment_type','cant_payments'], right_on=['payment_type','cant_payments'], how = 'left').drop_duplicates()

        df_factSubscription = df_factSubscription.groupby(['id_date','id_student','id_event','id_payment_method','id_frequency']).agg({"value":['sum','count']}).reset_index()
        df_factSubscription.columns = ['id_date','id_student','id_event','id_payment_method','id_frequency','value_sum','value_count']
        df_factSubscription.to_csv('./test/test.csv')
        df_factSubscription = df_factSubscription.assign(date_created = date , date_updated = date).drop_duplicates()

        # Fact usability
        df_enrollment_class['id_date']= pd.to_datetime(df_enrollment_class['created_at']).dt.strftime('%Y%m%d')
        df_factUsability = pd.merge(df_enrollment_class, df_dimClass, left_on='name_class', right_on='name_class', how = 'left').drop_duplicates()
        df_factUsability = pd.merge(df_factUsability, df_dimStudents, left_on='id_student', right_on='id', how = 'left').drop_duplicates()
        df_factUsability = pd.merge(df_factUsability, df_courses, left_on='name_course', right_on='name_course', how = 'left').drop_duplicates()
        
        df_factUsability = df_factUsability.loc[:,['id_date','id_student_y','id_class','duration']]
        df_factUsability['flag_complete'] = pd.Series([1 for x in range(len(df_factUsability.index))]) 
        df_factUsability.columns = ['id_date','id_student','id_class','duration','flag_complete']
        df_factUsability = df_factUsability.assign(date_created = date , date_updated = date)

        df_fact=[df_factSubscription,df_factUsability]    
        print(date + ' - Fact tables has been updated!')

    except Exception as e:
        print(date + ' - ERROR updating Fact Tables: ' + str(e))

    return df_dim , df_fact



def load(df_dim,df_fact):
    """
        This function load data to redshift data base.
        Here we update tables into dimentional model in Redshift
    """
    df_dimStudents = df_dim[0]
    df_dimPaymenthMethod = df_dim[1]
    df_dimClass = df_dim[2]
    df_dimEvent = df_dim[3]
    df_dimFrequency = df_dim[4]
    df_dimTime = df_dim[5]
    
    df_factSubscription = df_fact[0]
    df_factUsability = df_fact[1]

    try:
        print('\n' + date + ' - Connecting to Redshift...')
        con = redshift_connector.connect(host='redshift-cluster.cjdkillol2ft.us-east-1.redshift.amazonaws.com',
                                         port = 5439,
                                         database='platzi',
                                         user='user_platzi',
                                         password='Platzi123')
        print(date + ' - Connected to Redshift!')

        with con.cursor() as cursor:

            # Student Dimention
            print('\n' + date + ' - Inserting dim_Student..')
            cursor.execute("DELETE FROM dwh.dim_Student")
            cursor.executemany("INSERT INTO dwh.dim_Student (code_student,first_name,last_name,phone,email,age,country,city,date_created,date_updated,id_student) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", df_dimStudents.values.tolist())
            con.commit()
            print(date + ' - dim_Student has been updated!')

            # Payment Method Dimention
            print(date + ' - Inserting dim_payment_method...')
            cursor.execute("DELETE FROM dwh.dim_payment_method")
            cursor.executemany("INSERT INTO dwh.dim_payment_method (payment_code, payment_name, currency, code, date_created , date_updated, id_payment_method) VALUES (%s, %s, %s, %s, %s, %s, %s)", df_dimPaymenthMethod.values.tolist())
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
            cursor.executemany("INSERT INTO dwh.dim_Event (code_event, type_event, duration_event, date_created, date_updated, id_event) VALUES (%s, %s, %s, %s, %s, %s)", df_dimEvent.values.tolist())
            con.commit()
            print(date + ' - dim_Event has been updated!')

            # Frequency Dimention
            print(date + ' - Inserting dim_Frequency..')
            cursor.execute("DELETE FROM dwh.dim_Frequency")
            cursor.executemany("INSERT INTO dwh.dim_Frequency (frequency_code, frequency_type, frequency_num, date_created, date_updated, id_frequency) VALUES (%s, %s, %s, %s, %s, %s)", df_dimFrequency.values.tolist())
            con.commit()
            print(date + ' - dim_Frequency has been updated!')

            # Date Dimention
            print(date + ' - Inserting dim_date..')
            cursor.execute("DELETE FROM dwh.dim_date")
            cursor.executemany("INSERT INTO dwh.dim_date ( id_date,date, day, week, month, quarter, year, date_created, date_updated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", df_dimTime.values.tolist())
            con.commit()
            print(date + ' - dim_date has been updated!')

            # Fact Subscription
            print('\n' + date + ' - Inserting fact_subscription..')
            cursor.execute("DELETE FROM dwh.fact_subscription")
            cursor.executemany("INSERT INTO dwh.fact_subscription (id_date, id_student ,id_event ,id_payment_method ,id_frequency ,value ,quantity ,date_created ,date_updated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", df_factSubscription.values.tolist())
            con.commit()
            print(date + ' - fact_subscription has been updated!')

            # Fact Usability
            print(date + ' - Inserting fact_usability..')
            cursor.execute("DELETE FROM dwh.fact_usability")
            cursor.executemany("INSERT INTO dwh.fact_usability (id_date, id_student ,id_class ,duration ,flag_complete ,date_created ,date_updated) VALUES (%s, %s, %s, %s, %s, %s, %s)", df_factUsability.values.tolist())
            con.commit()
            print(date + ' - fact_usability has been updated!')

    except Exception as e:
        print(date + ' - Connection ERROR: ' + str(e))



def main():
    print('\n' + date + ' - The ETL has started!!')

    df_extract = extract()
    df_dim,df_fact = transform(df_extract)
    load(df_dim,df_fact)

    print('\n' + date + ' - The ETL has finished!!')


if __name__ == '__main__':
    main()


