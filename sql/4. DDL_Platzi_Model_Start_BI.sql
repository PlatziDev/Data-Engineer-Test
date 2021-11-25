DROP TABLE IF EXISTS fac_event;
DROP TABLE IF EXISTS dim_event_type;
DROP TABLE IF EXISTS dim_subscription_type;
DROP TABLE IF EXISTS dim_user_subscription;
DROP TABLE IF EXISTS dim_payment;


CREATE TABLE dim_event_type
(
    id_event_type       INT NOT NULL distkey sortkey,
    name                CHARACTER(100) NOT NULL,
    status              BOOLEAN NOT NULL ,
    PRIMARY KEY(id_event_type)
);

CREATE TABLE dim_subscription_type
(
    id_subscription_type        INT NOT NULL distkey sortkey,
    name                        CHARACTER(100) NOT NULL,
    description                 CHARACTER(200) NOT NULL ,
    PRIMARY KEY(id_subscription_type)
);

CREATE TABLE dim_user_subscription
(
    id_subscription         INT NOT NULL distkey sortkey,
    description             CHARACTER(200) NOT NULL,
    benefits                TEXT NOT NULL,
    first_name              CHARACTER(50) NOT NULL ,
	middle_name             CHARACTER(50) ,
	last_name               CHARACTER(50) NOT NULL ,
	email                   CHARACTER(50) NOT NULL ,
	bio                     TEXT ,
	PRIMARY KEY(id_subscription)
);

CREATE TABLE dim_payment
(
    id_payment                  INT NOT NULL distkey sortkey,
    payment_method              CHARACTER(100) NOT NULL,
    payment_classification      CHARACTER(100) NOT NULL,
    currency_iso                CHARACTER(20) NOT NULL,
    currency_name               CHARACTER(100) NOT NULL,
    identity_card               CHARACTER(12) ,
	cardholder_name             CHARACTER(50) ,
	card_number                 CHARACTER(16) ,
	token_transaction           CHARACTER(100) NOT NULL ,
	status_code                 CHARACTER(20) NOT NULL ,
	expiry_date                 DATE ,
	security_code               CHARACTER(20) ,
	PRIMARY KEY(id_payment)
);

CREATE TABLE fac_event
(
	id_event_type               INT NOT NULL distkey sortkey,
	id_payment                  INT NULL ,
	id_subscription             INT NOT NULL ,
	id_subscription_type        INT NOT NULL ,
	event_timestamp             TIMESTAMP NOT NULL ,
	subscription_start_date     DATE NOT NULL ,
	subscription_end_date       DATE NOT NULL ,
	amount_payment              DECIMAL(16,4) NULL ,
	status                      BOOLEAN,
	PRIMARY KEY(id_event_type, id_payment, id_subscription, id_subscription_type)
);

ALTER TABLE fac_event ADD CONSTRAINT fk_event_type FOREIGN KEY (id_event_type)
REFERENCES dim_event_type (id_event_type);

ALTER TABLE fac_event ADD CONSTRAINT fk_event_subscription FOREIGN KEY (id_subscription)
REFERENCES dim_user_subscription (id_subscription);

ALTER TABLE fac_event ADD CONSTRAINT fk_event_subs_type FOREIGN KEY (id_subscription_type)
REFERENCES dim_subscription_type (id_subscription_type);

ALTER TABLE fac_event ADD CONSTRAINT fk_event_payment FOREIGN KEY (id_payment)
REFERENCES dim_payment (id_payment);

