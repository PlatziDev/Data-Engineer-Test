# import configparser

# # CONFIG
# config = configparser.ConfigParser()
# config.read('dwh.cfg')
#
# HOST = config['DB']['HOST']
# USER = config['DB']['DB_USER']
# DB_NAME = config['DB']['DB_NAME']
# DB_PASSWORD = config['DB']['DB_PASSWORD']
# DB_PORT = config['DB']['DB_PORT']


# DROP TABLES

staging_students_drop = "DROP TABLE IF EXISTS stage_students;"
staging_subscriptions_drop = "DROP TABLE IF EXISTS stage_subscriptions;"
staging_sub_types_drop = "DROP TABLE IF EXISTS stage_subs_types;"
staging_sub_codes_drop = "DROP TABLE IF EXISTS stage_subs_codes;"
staging_payments_drop = "DROP TABLE IF EXISTS stage_payments;"
staging_transactions_drop = "DROP TABLE IF EXISTS stage_transactions;"
staging_enrollment_drop = "DROP TABLE IF EXISTS stage_enrollment;"
staging_courses_drop = "DROP TABLE IF EXISTS stage_courses;"
staging_classes_drop = "DROP TABLE IF EXISTS stage_classes;"
staging_schools_drop = "DROP TABLE IF EXISTS stage_schools;"


# CREATE TABLES

staging_students_create = ("""CREATE TABLE IF NOT EXISTS stage_students (
	student_id INT PRIMARY KEY,
	firstName VARCHAR,
	gender VARCHAR,
	lastName VARCHAR,
    location VARCHAR,
    email VARCHAR,
    birthdate DATE,
    last_login DATE)
""")

staging_subscriptions_create = ("""CREATE TABLE IF NOT EXISTS stage_subscriptions (
	subscription_id INT PRIMARY KEY
	student_id INT FOREIGN KEY,
	payment_id INT FOREIGN KEY,
	status_code_id INT FOREIGN KEY,
	status_type_id INT FOREIGN KEY,
	start_date DATE,
	end_date DATE)
""")

staging_sub_types_create = ("""CREATE TABLE IF NOT EXISTS stage_subs_types (
	sub_type_id INT PRIMARY KEY,
	sub_level VARCHAR,
	description VARCHAR,
	price NUMERIC
	)""")

staging_sub_codes_create = ("""CREATE TABLE IF NOT EXISTS stage_subs_types (
	sub_code_id INT PRIMARY KEY,
	sub_status VARCHAR,
	description VARCHAR
	)""")

staging_payments_create = ("""CREATE TABLE IF NOT EXISTS payments (
	payment_id INT PRIMARY KEY,
	method VARCHAR,
	status_code VARCHAR,
	transaction_id INT FOREIGN)
""")

staging_transactions_create = ("""CREATE TABLE IF NOT EXISTS transactions (
	transaction_id INT PRIMARY KEY,
	description VARCHAR,
	status VARCHAR,
	currency VARCHAR,
	amount NUMERIC,
	transaction_date DATE NOT NULL)
""")

staging_enrollment_create = ("""CREATE TABLE IF NOT EXISTS enrollment (
	enrollment_id INT PRIMARY KEY,
	course_id INT FOREIGN KEY,
	student_id INT FEORIGN KEY,
    n_courses INT,
	start_date DATE,
	end_date DATE
	)
""")

staging_courses_create = ("""CREATE TABLE IF NOT EXISTS courses (
	course_id INT PRIMARY KEY,
	school_id INT FEORIGN KEY,
	name VARCHAR,
	description VARCHAR,
    class_id INT FOREIGN KEY,
    completed_flag BOOLEAN
	)
""")

staging_schools_create = ("""CREATE TABLE IF NOT EXISTS schools (
	school_id INT FOREIGN KEY,
	name VARCHAR,
	description VARCHAR,
	degree VARCHAR
	)
""")

staging_classes_create = ("""CREATE TABLE IF NOT EXISTS classes (
	class_id INT PRIMARY KEY,
	name VARCHAR,
	description VARCHAR,
    course_type VARCHAR,
	duration NUMERIC,
    status VARCHAR
	)
""")

# QUERY LISTS

create_table_queries = [
    staging_students_create,
    staging_enrollment_create,
    staging_courses_create,
    staging_schools_create,
    staging_classes_create
    staging_payments_create,
    staging_sub_codes_create,
    staging_sub_types_create,
    staging_subscriptions_create,
    staging_transactions_create]

drop_table_queries = [
    staging_students_drop,
    staging_enrollment_drop,
    staging_courses_drop,
    staging_schools_drop,
    staging_payments_drop,
    staging_sub_codes_drop,
    staging_sub_types_drop,
    staging_subscriptions_drop,
    staging_transactions_drop,
    staging_classes_drop]
