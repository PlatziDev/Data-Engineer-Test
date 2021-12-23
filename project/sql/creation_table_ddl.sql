CREATE SCHEMA platzi;

CREATE TABLE platzi.students(
   student_id VARCHAR(255)  NOT NULL PRIMARY KEY
  ,name       VARCHAR(255) NOT NULL
  ,surname    VARCHAR(255) NOT NULL
  ,full_name  VARCHAR(255) NOT NULL
  ,email      VARCHAR(255) NOT NULL
);
CREATE TABLE platzi.subscriptions(
   subscription_id VARCHAR(255)  NOT NULL PRIMARY KEY
  ,usd_price       VARCHAR(255) NOT NULL
  ,description     VARCHAR(255) NOT NULL
);

CREATE TABLE platzi.extra_events(
   extra_event_id VARCHAR(255)  NOT NULL PRIMARY KEY
  ,type           VARCHAR(255) NOT NULL
  ,url            VARCHAR(1285) NOT NULL
  ,name           VARCHAR(52) NOT NULL
  ,description    VARCHAR(255) NOT NULL
);
CREATE TABLE platzi.schools(
   school_id   VARCHAR(255)  NOT NULL PRIMARY KEY
  ,name        VARCHAR(37) NOT NULL
  ,description VARCHAR(60) NOT NULL
);
CREATE TABLE platzi.courses(
   course_id   VARCHAR(255)  NOT NULL PRIMARY KEY
  ,school_id   VARCHAR(255)  NOT NULL
  ,name        VARCHAR(38) NOT NULL
  ,description VARCHAR(59) NOT NULL,
     CONSTRAINT fk_school_id
   FOREIGN KEY(school_id)
   REFERENCES schools(school_id)
);
CREATE TABLE platzi.classes(
   class_id    VARCHAR(255)  NOT NULL PRIMARY KEY
  ,course_id   VARCHAR(255)  NOT NULL
  ,name        VARCHAR(255) NOT NULL
  ,duration    VARCHAR(255)  NOT NULL
  ,description VARCHAR(255) NOT NULL,
   CONSTRAINT fk_course_id
   FOREIGN KEY(course_id)
   REFERENCES courses(course_id)
);


CREATE TABLE platzi.students_classes(
   student_id VARCHAR(255)  NOT NULL
  ,class_id   VARCHAR(255)  NOT NULL,
     CONSTRAINT fk_student
   FOREIGN KEY(student_id)
   REFERENCES students(student_id),
     CONSTRAINT fk_class_id
   FOREIGN KEY(class_id)
   REFERENCES classes(class_id)
);

CREATE TABLE platzi.students_courses(
   student_id VARCHAR(255)  NOT NULL
  ,course_id   VARCHAR(255)  NOT NULL,
     CONSTRAINT fk_student
   FOREIGN KEY(student_id)
   REFERENCES students(student_id),
     CONSTRAINT fk_course_id
   FOREIGN KEY(course_id)
   REFERENCES courses(course_id)
);

CREATE TABLE platzi.students_extra_events(
   student_id VARCHAR(255)  NOT NULL
  ,extra_event_id   VARCHAR(255)  NOT NULL,
     CONSTRAINT fk_student
   FOREIGN KEY(student_id)
   REFERENCES students(student_id),
     CONSTRAINT fk_extra_event_id
   FOREIGN KEY(extra_event_id)
   REFERENCES extra_events(extra_event_id)
);

CREATE TABLE platzi.students_schools(
   student_id VARCHAR(255)  NOT NULL
  ,school_id   VARCHAR(255)  NOT NULL,
       CONSTRAINT fk_student
   FOREIGN KEY(student_id)
   REFERENCES students(student_id),
     CONSTRAINT fk_school_id
   FOREIGN KEY(school_id)
   REFERENCES schools(school_id)
);

CREATE TABLE platzi.subscription_states(
   subscription_id          VARCHAR(255)  NOT NULL
  ,student_id               VARCHAR(255)  NOT NULL
  ,subscription_type        VARCHAR(255) NOT NULL
  ,subscription_state_value VARCHAR(255)  NOT NULL
  ,start_date               DATE  NOT NULL
  ,end_date                 DATE  NOT NULL
  ,payment_date             DATE  NOT NULL,
     CONSTRAINT fk_student
   FOREIGN KEY(student_id)
   REFERENCES students(student_id),
     CONSTRAINT fk_subscription_id
   FOREIGN KEY(subscription_id)
   REFERENCES subscriptions(subscription_id)
);

CREATE TABLE platzi.payment_methods(
   payment_method_id   VARCHAR(255)  NOT NULL PRIMARY KEY
  ,student_id          VARCHAR(255)  NOT NULL
  ,subscription_id     VARCHAR(255)  NOT NULL
  ,payment_method_type VARCHAR(255) NOT NULL
  ,description         VARCHAR(255) NOT NULL
  ,currency_price      VARCHAR(255) NOT NULL
  ,usd_price           VARCHAR(255) NOT NULL
  ,currency            VARCHAR(255) NOT NULL
  ,payment_date        DATE  NOT NULL,
   CONSTRAINT fk_student
   FOREIGN KEY(student_id)
   REFERENCES students(student_id),
   CONSTRAINT fk_subscription_id
   FOREIGN KEY(subscription_id)
   REFERENCES subscriptions(subscription_id)
);