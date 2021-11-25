DROP TABLE IF EXISTS t_subscription_event;
DROP TABLE IF EXISTS t_payment_detail;
DROP TABLE IF EXISTS t_currency;
DROP TABLE IF EXISTS t_payment_method;
DROP TABLE IF EXISTS t_payment_classification;
DROP TABLE IF EXISTS t_subscription;
DROP TABLE IF EXISTS t_subscription_type;
DROP TABLE IF EXISTS t_event_type;
DROP TABLE IF EXISTS t_school_course;
DROP TABLE IF EXISTS t_enrollment_school;
DROP TABLE IF EXISTS t_school;
DROP TABLE IF EXISTS t_enrollment_course;
DROP TABLE IF EXISTS t_enrollment_class;
DROP TABLE IF EXISTS t_class;
DROP TABLE IF EXISTS t_course;
DROP TABLE IF EXISTS t_course_type;
DROP TABLE IF EXISTS t_site_content_access_history;
DROP TABLE IF EXISTS t_user;
DROP TABLE IF EXISTS t_site_content;
DROP TABLE IF EXISTS t_site_content_type;

CREATE TABLE t_class
(
	id_class              SERIAL NOT NULL ,
	id_course             INT NOT NULL ,
	name                  CHARACTER(200) NOT NULL ,
	description           TEXT NOT NULL ,
	duration              TIME NOT NULL ,
	url_blob              CHARACTER(500) ,
	publish_date          DATE NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_class)
);

CREATE TABLE t_course
(
	id_course             SERIAL NOT NULL ,
	id_course_type        INT NOT NULL ,
	name                  CHARACTER(50) NOT NULL ,
	description           CHARACTER(300) ,
	estimated_duration    TIME ,
	publish_date          DATE NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_course)
);

CREATE TABLE t_course_type
(
	id_course_type        SERIAL NOT NULL ,
	description           CHARACTER(50) NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_course_type)
);

CREATE TABLE t_currency
(
	id_currency           SERIAL NOT NULL ,
	iso                   CHARACTER(5) NOT NULL ,
	name                  CHARACTER(20) NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_currency)
);

CREATE TABLE t_enrollment_class
(
	id_user               INT NOT NULL ,
	id_class              INT NOT NULL ,
	completed             BOOLEAN NOT NULL ,
	enrollment_date       DATE NOT NULL ,
	time_remaining        TIME NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY (id_user, id_class)
);

CREATE TABLE t_enrollment_course
(
	id_user               INT NOT NULL ,
	id_course             INT NOT NULL ,
	enrollment_date       DATE NOT NULL ,
    completed             BOOLEAN NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY (id_user, id_course)
);

CREATE TABLE t_enrollment_school
(
	id_user               INT NOT NULL ,
	id_school             INT NOT NULL ,
	enrollment_date       DATE NOT NULL ,
	completed             BOOLEAN ,
	status                BOOLEAN NOT NULL ,
	updated_at            DATE NOT NULL ,
	created_at            DATE NOT NULL ,
	PRIMARY KEY (id_user, id_school)
);

CREATE TABLE t_event_type
(
	id_event_type         SERIAL NOT NULL ,
	description           CHARACTER(50) NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_event_type)
);

CREATE TABLE t_payment_classification
(
	id_payment_classification  SERIAL NOT NULL ,
	name                  CHARACTER(50) NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_payment_classification)
);

CREATE TABLE t_payment_method
(
	id_payment_method     SERIAL NOT NULL ,
	id_payment_classification  INT NOT NULL ,
	name                  CHARACTER(50) NOT NULL ,
	description           CHARACTER(200) ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_payment_method)
);

CREATE TABLE t_payment_detail
(
	id_payment_detail  SERIAL NOT NULL ,
	id_currency           INT NOT NULL ,
	id_payment_method     INT NOT NULL ,
	identity_card         CHARACTER(12) ,
	cardholder_name       CHARACTER(50) ,
	card_number           CHARACTER(16) ,
	token_transaction     CHARACTER(100) NOT NULL ,
	status_code           CHARACTER(20) NOT NULL ,
	transaction_timestamp  TIMESTAMP NOT NULL ,
	amount                DECIMAL(16,4) NOT NULL ,
	expiry_date           DATE ,
	security_code         CHARACTER(20) ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_payment_detail)
);

CREATE TABLE t_school
(
	id_school             SERIAL NOT NULL ,
	name                  CHARACTER(50) ,
	description           CHARACTER(100) ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_school)
);

CREATE TABLE t_school_course
(
	id_school             INT NOT NULL ,
	id_course             INT NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_school, id_course)
);

CREATE TABLE t_site_content
(
	id_site_content       SERIAL NOT NULL ,
	id_site_content_type  INT NOT NULL ,
	slug                  CHARACTER(200) NOT NULL ,
	name                  CHARACTER(200) NOT NULL ,
	description           CHARACTER(500) ,
	content               TEXT NOT NULL ,
	publish_date          DATE NOT NULL ,
	url_stream            CHARACTER(200) ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_site_content)
);

CREATE TABLE t_site_content_access_history
(
	id_site_content_access_history  SERIAL NOT NULL ,
	access_date           DATE NOT NULL ,
	id_site_content       SERIAL NOT NULL ,
	id_user               SERIAL NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_site_content_access_history)
);

CREATE TABLE t_site_content_type
(
	id_site_content_type  SERIAL NOT NULL ,
	name                  CHARACTER(50) NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_site_content_type)
);

CREATE TABLE t_subscription
(
	id_subscription       SERIAL NOT NULL ,
	id_user               INT NOT NULL UNIQUE,
	description           TEXT NOT NULL ,
	price                 DECIMAL(16,4) ,
	benefits              TEXT ,
	id_subscription_type  SERIAL NOT NULL ,
	subscription_start_date  DATE NOT NULL ,
	subscription_end_date  DATE NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            CHAR(18) NOT NULL ,
	PRIMARY KEY(id_subscription)
);

CREATE TABLE t_subscription_event
(
	id_subscription_event  SERIAL NOT NULL ,
	id_subscription       INT NOT NULL ,
	id_event_type         INT NOT NULL ,
	id_payment_detail     INT NULL ,
	id_subscription_type  INT NOT NULL,
	event_timestamp       TIMESTAMP NOT NULL ,
	subscription_start_date  DATE NOT NULL ,
	subscription_end_date  DATE NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_subscription_event)
);

CREATE TABLE t_subscription_type
(
	id_subscription_type  SERIAL NOT NULL ,
	name                  CHARACTER(50) NOT NULL ,
	description           CHARACTER(100) NOT NULL ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_subscription_type)
);

CREATE TABLE t_user
(
	id_user               SERIAL NOT NULL ,
	first_name            CHARACTER(50) NOT NULL ,
	middle_name           CHARACTER(50) ,
	last_name             CHARACTER(50) NOT NULL ,
	email                 CHARACTER(50) NOT NULL ,
	password              CHARACTER(256) NOT NULL ,
	bio                   TEXT ,
	status                BOOLEAN NOT NULL ,
	created_at            DATE NOT NULL ,
	updated_at            DATE NOT NULL ,
	PRIMARY KEY(id_user)
);

ALTER TABLE t_payment_method ADD CONSTRAINT fk_payment_method_classification FOREIGN KEY (id_payment_classification)
REFERENCES t_payment_classification (id_payment_classification);

ALTER TABLE t_payment_detail ADD CONSTRAINT fk_payment_deatil_method FOREIGN KEY (id_payment_method)
REFERENCES t_payment_method (id_payment_method);

ALTER TABLE t_payment_detail ADD CONSTRAINT fk_payment_deatil_currency FOREIGN KEY (id_currency)
REFERENCES t_currency (id_currency);

ALTER TABLE t_subscription_event ADD CONSTRAINT fk_subscription_event_transaction FOREIGN KEY (id_payment_detail)
REFERENCES t_payment_detail (id_payment_detail);

ALTER TABLE t_subscription_event ADD CONSTRAINT fk_subscription_event_subscription FOREIGN KEY (id_subscription)
REFERENCES t_subscription (id_subscription);

ALTER TABLE t_subscription_event ADD CONSTRAINT fk_subscription_event_event_type FOREIGN KEY (id_event_type)
REFERENCES t_event_type (id_event_type);

ALTER TABLE t_subscription_event ADD CONSTRAINT fk_subscription_event_subs_type FOREIGN KEY (id_subscription_type)
REFERENCES t_subscription_type (id_subscription_type);

ALTER TABLE t_subscription ADD CONSTRAINT fk_subscription_type FOREIGN KEY (id_subscription_type)
REFERENCES t_subscription_type (id_subscription_type);

ALTER TABLE t_subscription ADD CONSTRAINT fk_subscription FOREIGN KEY (id_user)
REFERENCES t_user (id_user);

ALTER TABLE t_site_content ADD CONSTRAINT fk_site_content_type FOREIGN KEY (id_site_content_type)
REFERENCES t_site_content_type (id_site_content_type);

ALTER TABLE t_site_content_access_history ADD CONSTRAINT fk_site_history_access_content FOREIGN KEY (id_site_content)
REFERENCES t_site_content (id_site_content);

ALTER TABLE t_site_content_access_history ADD CONSTRAINT fk_site_history_access_user FOREIGN KEY (id_user)
REFERENCES t_user (id_user);

ALTER TABLE t_enrollment_school ADD CONSTRAINT fk_enrollment_school_user FOREIGN KEY (id_user)
REFERENCES t_user (id_user);

ALTER TABLE t_enrollment_school ADD CONSTRAINT fk_enrollment_school_school FOREIGN KEY (id_school)
REFERENCES t_school (id_school);

ALTER TABLE t_enrollment_course ADD CONSTRAINT fk_enrollment_course_user FOREIGN KEY (id_user)
REFERENCES t_user (id_user);

ALTER TABLE t_enrollment_course ADD CONSTRAINT fk_enrollment_course_course FOREIGN KEY (id_course)
REFERENCES t_course (id_course);

ALTER TABLE t_enrollment_class ADD CONSTRAINT fk_enrollment_class_user FOREIGN KEY (id_user)
REFERENCES t_user (id_user);

ALTER TABLE t_enrollment_class ADD CONSTRAINT fk_enrollment_class_class FOREIGN KEY (id_class)
REFERENCES t_class (id_class);

ALTER TABLE t_school_course ADD CONSTRAINT fk_school_course_school FOREIGN KEY (id_school)
REFERENCES t_school (id_school);

ALTER TABLE t_school_course ADD CONSTRAINT fk_school_course_course FOREIGN KEY (id_course)
REFERENCES t_course (id_course);

ALTER TABLE t_course ADD CONSTRAINT fk_course_type FOREIGN KEY (id_course_type)
REFERENCES t_course_type (id_course_type);

ALTER TABLE t_class ADD CONSTRAINT fk_class_course FOREIGN KEY (id_course)
REFERENCES t_course (id_course);
