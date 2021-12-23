import pandas as pd
from cli.model.rm import Clas
from cli.model.rm import Course
from cli.model.rm import Currency
from cli.model.rm import Payment
from cli.model.rm import Paymentmethod
from cli.model.rm import School
from cli.model.rm import Sitecontent
from cli.model.rm import Sitenavigationhistory
from cli.model.rm import Student
from cli.model.rm import Studentinscription
from cli.model.rm import Subscriptiontype
from cli.model.rm import Subscriptionevent
from cli.model.rm import Subscriptioneventtype
from cli.model.rm import Subscription

from cli.db import Session, engine, Base
import os
def load_all_csv():
    try:
        load_from_csv('/dataset/Student.csv')        
        load_from_csv('/dataset/SubscriptionType.csv')
        load_from_csv('/dataset/Subscription.csv')
        load_from_csv('/dataset/SubscriptionEventType.csv')
        load_from_csv('/dataset/SubscriptionEvent.csv')
        load_from_csv('/dataset/School.csv')
        load_from_csv('/dataset/Course.csv')
        load_from_csv('/dataset/Class.csv')
        load_from_csv('/dataset/Currency.csv')        
        load_from_csv('/dataset/PaymentMethod.csv')
        load_from_csv('/dataset/Payment.csv')
        load_from_csv('/dataset/SiteContent.csv')
        load_from_csv('/dataset/SiteNavigationHistory.csv')
        load_from_csv('/dataset/StudentInscription.csv')        
        
    except Exception as e :
        print(e)

def load_from_csv(file_name):
    model = os.path.splitext(os.path.basename(file_name))[0]
    Base.metadata.create_all(engine)
    print("Loading ",model, " from ", file_name)
    session = Session()

    try:
        data = pd.read_csv(file_name)
        for i, row in data.iterrows():
            print(row)
            if model == 'Student':
                student = Student(row['id'],row['first_name'],row['last_name'],row['nickname'],row['email'],row['birthday'],row['created_at'],row['updated_at'],row['status'])
                session.add(student)
            elif model == 'Subscription':
                subscription = Subscription(row['id'],row['student_id'],row['subscription_type_id'],row['start_date'],row['end_date'],row['created_at'],row['updated_at'],row['status'])
                session.add(subscription)
            elif model == 'SubscriptionType':
                subscriptiontype = Subscriptiontype(row['id'],row['name'],row['description'],row['created_at'],row['updated_at'],row['status'])
                session.add(subscriptiontype)
            elif model == 'SubscriptionEvent':
                subscriptionevent = Subscriptionevent(row['id'],row['subscription_id'],row['subscription_event_type_id'],row['description'],row['duration'],row['event_timestamp'],row['created_at'],row['updated_at'])
                session.add(subscriptionevent)
            elif model == 'SubscriptionEventType':
                subscriptioneventtype = Subscriptioneventtype(row['id'],row['name'],row['description'],row['created_at'],row['updated_at'])
                session.add(subscriptioneventtype)
            elif model == 'SubscriptionEvent':
                subscriptionevent = Subscriptionevent(row['id'],row['name'],row['description'],row['description'],row['created_at'],row['updated_at'])
                session.add(subscriptionevent)                
            elif model == 'Payment':
                payment = Payment(row['id'],row['subscription_id'],row['student_id'],row['method_id'],row['currency_id'],row['amount'],row['transaction_date'],row['created_at'],row['updated_at'],row['status'])
                session.add(payment) 
            elif model == 'Currency':
                currency = Currency(row['id'],row['name'],row['description'],row['territory'],row['fractional_unit'],row['iso_code'],row['created_at'],row['updated_at'],row['status'])
                session.add(currency)
            elif model == 'PaymentMethod':
                paymentmethod = Paymentmethod(row['id'],row['name'],row['description'],row['version'],row['created_at'],row['updated_at'],row['status'])
                session.add(paymentmethod)                
            elif model == 'StudentInscription':
                studentinscription = Studentinscription(row['id'],row['class_id'],row['course_id'],row['school_id'],row['student_id'],row['created_at'],row['updated_at'],row['status'])
                session.add(studentinscription)  
            elif model == 'Class':
                clas = Clas(row['id'],row['course_id'],row['name'],row['description'],row['created_at'],row['updated_at'],row['status'])
                session.add(clas)  
            elif model == 'Course':
                course = Course(row['id'],row['school_id'],row['name'],row['description'],row['created_at'],row['updated_at'],row['status'])
                session.add(course)
            elif model == 'School':
                school = School(row['id'],row['name'],row['description'],row['created_at'],row['updated_at'],row['status'])
                session.add(school) 
            elif model == 'SiteNavigationHistory':
                sitenavegationhistory = Sitenavigationhistory(row['id'],row['student_id'],row['content_id'],row['created_at'],row['updated_at'],row['status'])
                session.add(sitenavegationhistory) 
            elif model == 'SiteContent':
                sitecontent = Sitecontent(row['id'],row['name'],row['description'],row['url'],row['type'],row['created_at'],row['updated_at'],row['status'])
                session.add(sitecontent)
        session.commit()
    except Exception as e :
        print(e)
        session.rollback()
    finally:
        session.close()        