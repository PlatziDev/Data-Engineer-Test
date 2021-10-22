import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

student_dim_create = ("""CREATE TABLE IF NOT EXISTS student_dim (
    student_key INT PRIMARY KEY,
    subscription_status VARCHAR,
    subscription_start_date_key DATE FOREIGN KEY,
    subscription_end_date_key DATE FOREIGN KEY,
    subscription_type VARCHAR
)""")

time_dim_create = ("""CREATE TABLE IF NOT EXISTS time_dim (
	time_key TIMESTAMP PRIMARY KEY,
	hour NUMERIC,
	day NUMERIC,
	week NUMERIC,
	month NUMERIC,
	year NUMERIC,
	weekday NUMERIC)
""")

class_dim_create = ("""CREATE TABLE IF NOT EXISTS classes_dim (
    class_key INT PRIMARY KEY,
    name VARCHAR,
    status_flag VARCHAR,
    start_date_key DATE FOREIGN KEY,
    end_date_key DATE FOREIGN KEY
)""")

def process_fact_tables(cur, filepath: str) -> None:
    """
    Function to process Subscription records and enrollment counts.
    """
    pass


def process_dimension_tables(cur, filepath: str) -> None:
    """
    Function to process each dimension table separately.

    ToDo: Add COPY statement functionality and tests of data.

    """
    pass



def run_insert():
    pass


def main():
    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config['DB'].values()))
    run_insert()

    conn.close()


if __name__ == "__main__":
    main()
