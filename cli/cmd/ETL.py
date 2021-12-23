from cli.db import Session,engine,Base
from sqlalchemy import func,desc,distinct,union_all,text

#--- Star Model
from cli.model.dwh import Factsubscription
from cli.model.dwh import Diminscription
from cli.model.dwh import Dimevent
from cli.model.dwh import Dimstudent
from cli.model.dwh import Dimpayment

def create_dwh_tables():
    create_dim_student()
    create_dim_inscription()
    create_fact_subscription()
    create_dim_payment()
    create_dim_event()

def create_dim_student():
    print("Ceated table DimStudent")
    session = Session()
    try:
        result = session.execute(text('''
        SELECT 
            id, first_name, last_name, status
        FROM
            challenge.Student
        '''))
        for row in result:
            dim_student = Dimstudent(row['id'],row['first_name'],row['last_name'],row['status'])
            session.add(dim_student)
        session.commit()
    except Exception as e :
        print(e)
        session.rollback()
    finally:
        session.close()

    return result.mappings().all()

def create_dim_inscription():
    print("Ceated table DimInscription")
    session = Session()
    try:
        result = session.execute(text('''
        SELECT 
            id, student_id, class_id, course_id, school_id, status,
            if (status = 'completed',1,0) as seen
        FROM
            challenge.StudentInscription
        '''))
        for row in result:
            dim_inscription = Diminscription(row['id'],row['student_id'],row['class_id'],row['course_id'],row['school_id'],row['status'],row['seen'])
            session.add(dim_inscription)
        session.commit()
    except Exception as e :
        print(e)
        session.rollback()
    finally:
        session.close()

    return result.mappings().all()    

def create_fact_subscription():
    print("Ceated table FactSubscription")
    session = Session()
    try:
        result = session.execute(text('''
        SELECT 
            SUB.id id,
            SUB.student_id student_id,
            SUB.subscription_type_id type,
            COU.qty_courtesy courtesy,
            PAU.qty_paused paused,
            SUB.start_date date,
            EXTRACT(DAY FROM SUB.start_date) day,
            EXTRACT(MONTH FROM SUB.start_date) month,
            EXTRACT(YEAR FROM SUB.start_date) year,
            EXTRACT(WEEK FROM SUB.start_date) week
        FROM
            challenge.Subscription SUB
                LEFT JOIN
            (SELECT 
                SEVT.subscription_id, COUNT(1) AS qty_paused
            FROM
                challenge.SubscriptionEvent SEVT
            LEFT JOIN challenge.SubscriptionEventType SETP ON SEVT.subscription_event_type_id = SETP.id
            WHERE
                SETP.name = 'Paused'
            GROUP BY SEVT.subscription_id) PAU ON PAU.subscription_id = SUB.id
                LEFT JOIN
            (SELECT 
                SEVT.subscription_id, COUNT(1) AS qty_courtesy
            FROM
                challenge.SubscriptionEvent SEVT
            LEFT JOIN challenge.SubscriptionEventType SETP ON SEVT.subscription_event_type_id = SETP.id
            WHERE
                SETP.name = 'Courtesy'
            GROUP BY SEVT.subscription_id) COU ON COU.subscription_id = SUB.id
            '''))
        for row in result:
            fact_subscription = Factsubscription(row['id'],row['student_id'],row['type'],row['courtesy'],row['paused'],row['date'],row['day'],row['month'],row['year'],row['week'])
            session.add(fact_subscription)
        session.commit()
    except Exception as e :
        print(e)
        session.rollback()
    finally:
        session.close()

    return result.mappings().all() 

def create_dim_payment():
    print("Ceated table DimPayment")
    session = Session()
    try:
        result = session.execute(text('''
        SELECT 
            PAY.id id,
            PAY.subscription_id subscription_id,
            PME.name method,
            CUR.name currency,
            PAY.amount amount,
            PAY.status status
        FROM
            challenge.Payment PAY
                LEFT JOIN
            challenge.PaymentMethod PME ON PAY.method_id = PME.id
                LEFT JOIN
            challenge.Currency CUR ON PAY.currency_id = CUR.id
        '''))
        for row in result:
            dim_payment = Dimpayment(row['id'],row['subscription_id'],row['method'],row['currency'],row['amount'],row['status'])
            session.add(dim_payment)
        session.commit()
    except Exception as e :
        print(e)
        session.rollback()
    finally:
        session.close()

    return result.mappings().all() 

def create_dim_event():
    print("Ceated table DimEvent")
    session = Session()
    try:
        result = session.execute(text('''
        SELECT 
            SE.id,
            SE.subscription_id,
            SE_T.name AS event_type,
            SE.event_timestamp,
            SE.description
        FROM
            challenge.SubscriptionEvent SE
                LEFT JOIN
            challenge.SubscriptionEventType SE_T ON SE.subscription_event_type_id = SE_T.id
            '''))
        for row in result:
            dim_event = Dimevent(row['id'],row['subscription_id'],row['event_type'],row['event_timestamp'],row['description'])
            session.add(dim_event)
        session.commit()
    except Exception as e :
        print(e)
        session.rollback()
    finally:
        session.close()

    return result.mappings().all()