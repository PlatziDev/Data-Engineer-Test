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


class Factsubscription(Base):

    __tablename__ = 'FactSubscription'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    student_id = Column(INTEGER, ForeignKey("DimStudent.id", name="fk_factSubscription_1"), nullable=False, index=True)
    type = Column(INTEGER, nullable=False)
    courtesy = Column(INTEGER, nullable=True)
    paused = Column(INTEGER, nullable=True)
    date = Column(DATE, nullable=False)
    day = Column(INTEGER, nullable=False)
    month = Column(INTEGER, nullable=False)
    year = Column(INTEGER, nullable=False)
    week = Column(INTEGER, nullable=False)

    dimstudent = relationship("Dimstudent", foreign_keys=[student_id], backref="factsubscription")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Factsubscription(%(id)s)>" % self.__dict__

    def __init__(self,id,student_id,type,courtesy,paused,date,day,month,year,week):
        self.id = id
        self.student_id = student_id
        self.type = type
        self.courtesy = courtesy
        self.paused = paused
        self.date = date
        self.day = day
        self.month = month
        self.year = year
        self.week = week     

class Diminscription(Base):

    __tablename__ = 'DimInscription'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    student_id = Column(INTEGER, ForeignKey("DimStudent.id", name="fk_DimInscription_1"), index=True)
    class_id = Column(INTEGER)
    course_id = Column(INTEGER)
    school_id = Column(INTEGER)
    status = Column(VARCHAR(45))
    seen = Column(INTEGER)

    dimstudent = relationship("Dimstudent", foreign_keys=[student_id], backref="diminscription")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Diminscription(%(id)s)>" % self.__dict__

    def __init__(self,id,student_id,class_id,course_id,school_id,status,seen):
        self.id = id
        self.student_id = student_id
        self.class_id = class_id
        self.course_id = course_id
        self.school_id = school_id
        self.status = status
        self.seen = seen
   
class Dimevent(Base):

    __tablename__ = 'DimEvent'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    subscription_id = Column(INTEGER, ForeignKey("FactSubscription.id", name="fk_DimEvent_1"), index=True)
    event_type = Column(VARCHAR(45))
    description = Column(VARCHAR(45))
    event_timestamp = Column(VARCHAR(45))

    factsubscription = relationship("Factsubscription", foreign_keys=[subscription_id], backref="dimevent")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Dimevent(%(id)s)>" % self.__dict__

    def __init__(self,id,subscription_id,event_type,description,event_timestamp):
        self.id = id
        self.subscription_id = subscription_id
        self.event_type = event_type
        self.description = description
        self.event_timestamp = event_timestamp

class Dimstudent(Base):

    __tablename__ = 'DimStudent'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    status = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Dimstudent(%(id)s)>" % self.__dict__

    def __init__(self,id,first_name,last_name,status):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.status = status

class Dimpayment(Base):

    __tablename__ = 'DimPayment'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(INTEGER, nullable=False, autoincrement=False, primary_key=True)  # pylint: disable=invalid-name
    subscription_id = Column(INTEGER, ForeignKey("FactSubscription.id", name="fk_DimPayment_1"), index=True)
    method = Column(VARCHAR(45))
    currency = Column(VARCHAR(45))
    amount = Column(INTEGER)
    status = Column(VARCHAR(45))

    factsubscription = relationship("Factsubscription", foreign_keys=[subscription_id], backref="dimpayment")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Dimpayment(%(id)s)>" % self.__dict__

    def __init__(self,id,subscription_id,method,currency,amount,status):
        self.id = id
        self.subscription_id = subscription_id
        self.method = method
        self.currency = currency
        self.amount = amount
        self.status = status
