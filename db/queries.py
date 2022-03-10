dimension_tables_query = """ 
CREATE TABLE student(
    id INT PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    user_name VARCHAR(30),
    gender VARCHAR(30),
    email VARCHAR(30),
    country VARCHAR(30),
    created_date DATE,
    status VARCHAR(30)
);

CREATE TABLE subscription_type(
    id INT PRIMARY KEY,
    name VARCHAR(30),
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE subscription(
    id INT PRIMARY KEY,
    student_id INT REFERENCES student(id),
    type_id INT REFERENCES subscription_type(id),
    start_date DATE,
    end_date DATE,
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE payment_method(
    id INT PRIMARY KEY,
    name VARCHAR(30),
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE payment_currency(
    id INT PRIMARY KEY,
    name VARCHAR(30),
    created_date DATE,
    status VARCHAR(30)
);

CREATE TABLE payment(
    id INT PRIMARY KEY,
    student_id INT REFERENCES student(id),
    currency_id INT REFERENCES payment_currency(id),
    method_id INT REFERENCES payment_method(id),
    subscription_id INT REFERENCES subscription(id),
    ammount NUMERIC(10,2),
    payment_date DATE,
    created_date DATE,
    status VARCHAR(30)
);

CREATE TABLE school(
    id INT PRIMARY KEY,
    name VARCHAR(30),
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE course(
    id INT PRIMARY KEY,
    school_id INT REFERENCES school(id),
    name VARCHAR(30),
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE class(
    id INT PRIMARY KEY,
    course_id INT REFERENCES course(id),
    name VARCHAR(30),
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE student_path(
    id INT PRIMARY KEY,
    student_id INT REFERENCES student(id),
    course_id INT REFERENCES course(id),
    school_id INT REFERENCES school(id),
    class_id INT REFERENCES class(id),
    created_date DATE,
    updated_date DATE,
    status VARCHAR(30)
);

CREATE TABLE student_progress(
	id INT PRIMARY KEY,
	student_id INT REFERENCES student(id),
	class_id INT REFERENCES class(id),
	created_date DATE,
	status VARCHAR(30)
);

CREATE TABLE subscription_history(
	id int PRIMARY KEY,
	subscription_id int REFERENCES subscription(id),
	type VARCHAR(30),
	created_date DATE
);
"""

fact_tables_query = """ 
    CREATE TABLE subscription_dim(
        subscription_id INT PRIMARY KEY,
        type VARCHAR(30)
    );

    CREATE TABLE payment_date_dim(
        payment_id INT PRIMARY KEY,
        "date" DATE,
        "day" INT,
        "week" INT,
        "month" INT,
        "year" INT
    );

    CREATE TABLE student_dim(
        student_id INT PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        user_name VARCHAR(30),
        country VARCHAR(30),
        gender VARCHAR(30),
        status VARCHAR(30)
    );

    CREATE TABLE sales_fact(
        id SERIAL PRIMARY KEY,
        payment_ammount NUMERIC(10,2),
        currency VARCHAR(30),
        payment_method VARCHAR(30),
        student_id INT REFERENCES student_dim(student_id),
        subscription_id INT REFERENCES subscription_dim(subscription_id),
        payment_id INT REFERENCES payment_date_dim(payment_id)
    );
 """

fact_sales_query = """ 
    SELECT p.ammount AS payment_ammount, pc.name AS currency, pm."name" AS payment_method, s.id AS student_id, sub.id AS subscription_id, p.id AS payment_id
    FROM student s 
    JOIN payment p ON p.student_id = s.id
    JOIN payment_method pm ON p.method_id = pm.id
    JOIN payment_currency pc ON p.currency_id = pc.id
    JOIN "subscription" sub ON s.id = sub.student_id 
 """

dim_subscription_query = """ 
    SELECT s.id AS subscription_id, st.name AS type
    FROM "subscription" s 
    JOIN subscription_type st ON s.type_id = st.id 
 """

dim_student_query = """ 
    SELECT id AS student_id, first_name, last_name, user_name, country, gender, status 
    FROM student s
"""

dim_payment_date_query = """ 
    SELECT id AS payment_id, payment_date 
    FROM payment p 
"""
