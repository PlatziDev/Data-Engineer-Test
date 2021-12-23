#!/usr/bin/env python
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from cli.db import Base

if os.environ.get('DB_TYPE', 'MySQL') == 'MySQL':
    from sqlalchemy.dialects.mysql import DATE, INTEGER, DATETIME, VARCHAR
else:
    from sqlalchemy import Integer, String as VARCHAR, Date as DATE, DateTime as DATETIME

    class INTEGER(Integer):
        def __init__(self, *args, **kwargs):
            super(Integer, self).__init__()  # pylint: disable=bad-super-call

class Student(Base):

    __tablename__ = 'Student'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    first_name = Column(VARCHAR(45), nullable=False)
    last_name = Column(VARCHAR(45), nullable=False)
    nickname = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)
    birthday = Column(VARCHAR(45), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Student(%(id)s)>" % self.__dict__

    def __init__(self,id,first_name,last_name,nickname,email,birthday,created_at,updated_at,status):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.email = email
        self.birthday = birthday
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status

class Subscription(Base):

    __tablename__ = 'Subscription'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    student_id = Column(INTEGER, ForeignKey("Student.id", name="fk_Subscription_1"), nullable=False)
    subscription_type_id = Column(
        INTEGER, ForeignKey("SubscriptionType.id", name="fk_Subscription_2"), nullable=False, index=True
    )
    start_date = Column(DATE, nullable=False)
    end_date = Column(DATE, nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    student = relationship("Student", foreign_keys=[student_id], backref="subscription")
    subscriptiontype = relationship("Subscriptiontype", foreign_keys=[subscription_type_id], backref="subscription")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Subscription(%(id)s)>" % self.__dict__

    def __init__(self,id,student_id,subscription_type_id,start_date,end_date,created_at,updated_at,status):
        self.id = id
        self.student_id = student_id
        self.subscription_type_id = subscription_type_id
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status        

class Subscriptiontype(Base):

    __tablename__ = 'SubscriptionType'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Subscriptiontype(%(id)s)>" % self.__dict__

    def __init__(self,id,name,description,created_at,updated_at,status):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status           

class Subscriptionevent(Base):

    __tablename__ = 'SubscriptionEvent'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    subscription_id = Column(
        INTEGER, ForeignKey("Subscription.id", name="fk_SubscriptionEvent_1"), nullable=False, index=True
    )
    subscription_event_type_id = Column(
        INTEGER, ForeignKey("SubscriptionEventType.id", name="fk_SubscriptionEvent_2"), nullable=False, index=True
    )
    description = Column(VARCHAR(100), nullable=False)
    duration = Column(INTEGER, nullable=False)
    event_timestamp = Column(DATETIME, nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)

    subscription = relationship("Subscription", foreign_keys=[subscription_id], backref="subscriptionevent")
    subscriptioneventtype = relationship(
        "Subscriptioneventtype", foreign_keys=[subscription_event_type_id], backref="subscriptionevent"
    )

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Subscriptionevent(%(id)s)>" % self.__dict__

    def __init__(self,id,subscription_id,subscription_event_type_id,description,duration,event_timestamp,created_at,updated_at):
        self.id = id
        self.subscription_id = subscription_id
        self.subscription_event_type_id = subscription_event_type_id
        self.description = description
        self.duration = duration
        self.event_timestamp = event_timestamp
        self.created_at = created_at
        self.updated_at = updated_at         

class Subscriptioneventtype(Base):

    __tablename__ = 'SubscriptionEventType'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Subscriptioneventtype(%(id)s)>" % self.__dict__

    def __init__(self,id,name,description,created_at,updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at    

class Payment(Base):

    __tablename__ = 'Payment'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    subscription_id = Column(INTEGER, ForeignKey("Subscription.id", name="fk_Payment_1"), nullable=False, index=True)
    student_id = Column(INTEGER, nullable=False)
    method_id = Column(INTEGER, ForeignKey("PaymentMethod.id", name="fk_Payment_3"), nullable=False, index=True)
    currency_id = Column(INTEGER, ForeignKey("Currency.id", name="fk_Payment_2"), nullable=False, index=True)
    amount = Column(INTEGER, nullable=False)
    transaction_date = Column(DATE, nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    subscription = relationship("Subscription", foreign_keys=[subscription_id], backref="payment")
    paymentmethod = relationship("Paymentmethod", foreign_keys=[method_id], backref="payment")
    currency = relationship("Currency", foreign_keys=[currency_id], backref="payment")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Payment(%(id)s)>" % self.__dict__

    def __init__(self,id,subscription_id,student_id,method_id,currency_id,amount,transaction_date,created_at,updated_at,status):
        self.id = id
        self.subscription_id = subscription_id
        self.student_id = student_id
        self.method_id = method_id
        self.currency_id = currency_id
        self.amount = amount
        self.transaction_date = transaction_date
        self.created_at = created_at
        self.updated_at = updated_at    
        self.status = status

class Currency(Base):

    __tablename__ = 'Currency'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    fractional_unit = Column(VARCHAR(45), nullable=False)
    iso_code = Column(VARCHAR(45), nullable=False)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    status = Column(VARCHAR(45), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Currency(%(id)s)>" % self.__dict__

    def __init__(self,id,name,description,territory,fractional_unit,iso_code,created_at,updated_at,status):
        self.id = id
        self.name = name
        self.description = description
        self.territory = territory
        self.fractional_unit = fractional_unit
        self.iso_code = iso_code
        self.created_at = created_at
        self.updated_at = updated_at    
        self.status = status

class Paymentmethod(Base):

    __tablename__ = 'PaymentMethod'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    version = Column(VARCHAR(45), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Paymentmethod(%(id)s)>" % self.__dict__

    def __init__(self,id,name,description,version,created_at,updated_at,status):
        self.id = id
        self.name = name
        self.description = description
        self.version = version
        self.created_at = created_at
        self.updated_at = updated_at    
        self.status = status

class Studentinscription(Base):

    __tablename__ = 'StudentInscription'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    class_id = Column(INTEGER, ForeignKey("Class.id", name="fk_StudentInscription_2"), nullable=False, index=True)
    course_id = Column(INTEGER, ForeignKey("Course.id", name="fk_StudentInscription_3"), nullable=False, index=True)
    school_id = Column(INTEGER, ForeignKey("School.id", name="fk_StrudentInscription_4"), nullable=False, index=True)
    student_id = Column(INTEGER, ForeignKey("Student.id", name="fk_StudentInscription_1"), nullable=False, index=True)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45), nullable=False)

    clas = relationship("Clas", foreign_keys=[class_id], backref="studentinscription")
    course = relationship("Course", foreign_keys=[course_id], backref="studentinscription")
    school = relationship("School", foreign_keys=[school_id], backref="studentinscription")
    student = relationship("Student", foreign_keys=[student_id], backref="studentinscription")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Studentinscription(%(id)s)>" % self.__dict__

    def __init__(self,id,class_id,course_id,school_id,student_id,created_at,updated_at,status):
        self.id = id
        self.class_id = class_id
        self.course_id = course_id
        self.school_id = school_id
        self.student_id = student_id     
        self.created_at = created_at
        self.updated_at = updated_at    
        self.status = status

class Clas(Base):

    __tablename__ = 'Class'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    course_id = Column(INTEGER, ForeignKey("Course.id", name="fk_Class_1"), nullable=False, index=True)
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    course = relationship("Course", foreign_keys=[course_id], backref="class")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Clas(%(id)s)>" % self.__dict__

    def __init__(self,id,course_id,name,description,created_at,updated_at,status):
        self.id = id
        self.course_id = course_id
        self.name = name
        self.description = description
        self.created_at = created_at     
        self.updated_at = updated_at    
        self.status = status

class Course(Base):

    __tablename__ = 'Course'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    school_id = Column(INTEGER, ForeignKey("School.id", name="fk_Course_1"), nullable=False, index=True)
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    school = relationship("School", foreign_keys=[school_id], backref="course")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Course(%(id)s)>" % self.__dict__

    def __init__(self,id,school_id,name,description,created_at,updated_at,status):
        self.id = id
        self.school_id = school_id
        self.name = name
        self.description = description
        self.created_at = created_at     
        self.updated_at = updated_at    
        self.status = status

class School(Base):

    __tablename__ = 'School'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(100), nullable=False)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<School(%(id)s)>" % self.__dict__

    def __init__(self,id,name,description,created_at,updated_at,status):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at     
        self.updated_at = updated_at    
        self.status = status

class Sitenavigationhistory(Base):

    __tablename__ = 'SiteNavigationHistory'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    student_id = Column(
        INTEGER, ForeignKey("Student.id", name="fk_SiteNavigationHistory_1"), nullable=False, index=True
    )
    content_id = Column(
        INTEGER, ForeignKey("SiteContent.id", name="fk_SiteNavigationHistory_2"), nullable=False, index=True
    )
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    student = relationship("Student", foreign_keys=[student_id], backref="sitenavigationhistory")
    sitecontent = relationship("Sitecontent", foreign_keys=[content_id], backref="sitenavigationhistory")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Sitenavigationhistory(%(id)s)>" % self.__dict__

    def __init__(self,id,student_id,content_id,created_at,updated_at,status):
        self.id = id
        self.student_id = student_id
        self.content_id = content_id
        self.created_at = created_at     
        self.updated_at = updated_at    
        self.status = status

class Sitecontent(Base):

    __tablename__ = 'SiteContent'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45))
    description = Column(VARCHAR(100))
    url = Column(VARCHAR(200))
    type = Column(VARCHAR(45))
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    status = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Sitecontent(%(id)s)>" % self.__dict__

    def __init__(self,id,name,description,url,type,created_at,updated_at,status):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.type = type                
        self.created_at = created_at     
        self.updated_at = updated_at    
        self.status = status        
