
insert into t_payment_classification (id_payment_classification, name, status, created_at, updated_at)
values (1, 'RECURRENTE', true, current_date, current_date);

insert into t_payment_classification (id_payment_classification, name, status, created_at, updated_at)
values (2, 'NO-RECURRENTE', true, current_date, current_date);

insert into t_currency (id_currency, iso, name, status, created_at, updated_at)
values(1, 'PEN', 'Nuevo Sol', true, current_date, current_date);

insert into t_currency (id_currency, iso, name, status, created_at, updated_at)
values(2, 'USD', 'Dolares americanos', true, current_date, current_date);

insert into t_site_content_type (id_site_content_type, name, status, created_at, updated_at)
values(1, 'BLOG', true, current_date, current_date);

insert into t_site_content_type (id_site_content_type, name, status, created_at, updated_at)
values(2, 'LIVE STREAM', true, current_date, current_date);

insert into t_course_type (id_course_type, description, status, created_at, updated_at)
values (1, 'BASICO', true, current_date, current_date);

insert into t_course_type (id_course_type, description, status, created_at, updated_at)
values (2, 'INTERMEDIO', true, current_date, current_date);

insert into t_course_type (id_course_type, description, status, created_at, updated_at)
values (3, 'AVANZADO', true, current_date, current_date);

insert into t_site_content (id_site_content, id_site_content_type, slug, name, description, content, publish_date,
                            url_stream, status, created_at, updated_at)
values (1, 2, 'que-es-el-meta-verso', '¿Qué es el meta verso de Facebook?', 'Facebook acaba de anunciar el meta verso....',
        'Lorem ipsum...', current_date, 'https://w3.content/#jd8i3l4jl34', true, current_date, current_date);

insert into t_site_content (id_site_content, id_site_content_type, slug, name, description, content, publish_date,
                            url_stream, status, created_at, updated_at)
values (2, 2, 'como-conseguir-trabajo-como-junior', '¿Cómo conseguir tabajo como junior?', 'Conseguir tabajo como..',
        '## Lorem ipsum markdown content...', current_date, NULL, true, current_date, current_date);

insert into t_user (id_user, first_name, middle_name, last_name, bio, email, password, status, created_at, updated_at)
values (1, 'Robert', 'Junior', 'Huaman Caceres', 'Software/Data Engineer', 'bj112143@gmail.com', 'jsdf32oixcgf32ljk',
        true, current_date, current_date);

insert into t_user (id_user, first_name, middle_name, last_name, bio, email, password, status, created_at, updated_at)
values (2, 'Bryanne', 'Jorbachok', 'Blakink', 'Devops Engineer', 'bryanne@gmail.com', 'jsdf32oixcgf32ljk',
        true, current_date, current_date);

insert into t_site_content_access_history (id_site_content_access_history, id_site_content, id_user, access_date, status,
            created_at, updated_at)
values (1, 2, 1, current_date, true, current_date, current_date);

insert into t_site_content_access_history (id_site_content_access_history, id_site_content, id_user, access_date, status,
            created_at, updated_at)
values (2, 2, 2, current_date, true, current_date, current_date);

insert into t_site_content_access_history (id_site_content_access_history, id_site_content, id_user, access_date, status,
            created_at, updated_at)
values (3, 1, 1, current_date, true, current_date, current_date);

insert into t_school (id_school, name, description, status, created_at, updated_at)
values (1, 'Escuela de BackEnd', 'La mejor escuela de backend', true, current_date, current_date);

insert into t_school (id_school, name, description, status, created_at, updated_at)
values (2, 'Escuela de Data Sciences', 'La mejor escuela de Data Sciences', true, current_date, current_date);

insert into t_course (id_course, id_course_type, name, description, estimated_duration, publish_date, status, created_at, updated_at)
values (1, 1, 'Introducción a Python', 'Introduccion a python', '05:00:00', current_date, true, current_date, current_date);

insert into t_course (id_course, id_course_type, name, description, estimated_duration, publish_date, status, created_at, updated_at)
values (2, 2, 'Patrones de diseño con Python', 'Patrones de diseño con python', '04:00:00', current_date, true, current_date, current_date);

insert into t_course (id_course, id_course_type, name, description, estimated_duration, publish_date, status, created_at, updated_at)
values (3, 3, 'Analisis de datos con Python', 'Analisis de datos python', '08:00:00', current_date, true, current_date, current_date);

insert into t_course (id_course, id_course_type, name, description, estimated_duration, publish_date, status, created_at, updated_at)
values (4, 2, 'Construccion de API con DJango', 'Construccion de API con DJango', '06:00:00', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (1, 1, 'Variables1', 'Variables', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (2, 1, 'Diccionarios', 'Diccionarios', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (3, 1, 'Classes', 'Classes', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (4, 1, 'POO', 'POO', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (5, 2, 'CLEAN CODE', 'CLEAN CODE', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (6, 2, 'SOLID', 'SOLID', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (7, 2, 'Programacion funcional', 'Programacion funcional', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (8, 2, 'TDD', 'TDD', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (9, 3, 'Pandas', 'Pandas', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (10, 3, 'PySpark', 'PySpark', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (11, 3, 'Graficos', 'Graficos', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (12, 3, 'Procesamiento', 'Procesamiento', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (13, 4, 'End Points', 'End Points', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (14, 4, 'Servicios', 'Servicios', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (15, 4, 'Microservicios', 'Microservicios', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_class (id_class, id_course, name, description, duration, url_blob, publish_date, status, created_at, updated_at)
values (16, 4, 'Optmizacion', 'Optmizacion', '00:30:00', 'https://ws3.blob/#3jklasdfoealp', current_date, true, current_date, current_date);

insert into t_school_course (id_school, id_course, status, created_at, updated_at)
values (1, 1, true, current_date, current_date);
insert into t_school_course (id_school, id_course, status, created_at, updated_at)
values (1, 2, true, current_date, current_date);
insert into t_school_course (id_school, id_course, status, created_at, updated_at)
values (1, 3, true, current_date, current_date);

insert into t_school_course (id_school, id_course, status, created_at, updated_at)
values (2, 1, true, current_date, current_date);
insert into t_school_course (id_school, id_course, status, created_at, updated_at)
values (2, 4, true, current_date, current_date);

insert into t_enrollment_school (id_user, id_school, enrollment_date, completed, status, created_at, updated_at)
values (1, 1, current_date, false, true, current_date, current_date);
insert into t_enrollment_school (id_user, id_school, enrollment_date, completed, status, created_at, updated_at)
values (1, 2, current_date, false, true, current_date, current_date);
insert into t_enrollment_school (id_user, id_school, enrollment_date, completed, status, created_at, updated_at)
values (2, 2, current_date, false, true, current_date, current_date);

insert into t_enrollment_course (id_user, id_course, enrollment_date, completed, status, created_at, updated_at)
values (1, 1, current_date, false, true, current_date, current_date);

insert into t_enrollment_course (id_user, id_course, enrollment_date, completed, status, created_at, updated_at)
values (1, 2, current_date, false, true, current_date, current_date);

insert into t_enrollment_course (id_user, id_course, enrollment_date, completed, status, created_at, updated_at)
values (1, 3, current_date, false, true, current_date, current_date);

insert into t_enrollment_course (id_user, id_course, enrollment_date, completed, status, created_at, updated_at)
values (2, 1, current_date, false, true, current_date, current_date);

insert into t_enrollment_course (id_user, id_course, enrollment_date, completed, status, created_at, updated_at)
values (2, 4, current_date, false, true, current_date, current_date);

insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 1, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 2, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 3, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 4, current_date, true, '00:00:00', true, current_date, current_date);

insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 5, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 6, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 7, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 8, current_date, true, '00:00:00', true, current_date, current_date);

insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 9, current_date, false, '00:25:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 10, current_date, false, '00:30:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 11, current_date, false, '00:30:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (1, 12, current_date, false, '00:30:00', true, current_date, current_date);

insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 1, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 2, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 3, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 4, current_date, true, '00:00:00', true, current_date, current_date);

insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 13, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 14, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 15, current_date, true, '00:00:00', true, current_date, current_date);
insert into t_enrollment_class (id_user, id_class, enrollment_date, completed, time_remaining, status, created_at, updated_at)
values (2, 16, current_date, false, '00:15:00', true, current_date, current_date);

insert into t_payment_method (id_payment_method, id_payment_classification, name, description, status, created_at, updated_at)
values (1, 1, 'TARJETAS', 'PAGOS CON VISA, MASTERD CARD, AMEX', true, current_date, current_date);

insert into t_payment_method (id_payment_method, id_payment_classification, name, description, status, created_at, updated_at)
values (2, 2, 'CRIPTOMONEDA', 'PAGOS CON BITCOIN', true, current_date, current_date);

insert into t_subscription_type (id_subscription_type, name, description, status, created_at, updated_at)
values (1, 'BASIC', 'PLAN BASICO', true, current_date, current_date);

insert into t_subscription_type (id_subscription_type, name, description, status, created_at, updated_at)
values (2, 'EXPERT', 'PLAN EXPERT', true, current_date, current_date);

insert into t_subscription_type (id_subscription_type, name, description, status, created_at, updated_at)
values (3, 'EXPERT+', 'PLAN EXPERT PLUS', true, current_date, current_date);

insert into t_subscription (id_subscription, id_subscription_type, id_user, description, price, benefits, subscription_start_date,
                            subscription_end_date, status, created_at, updated_at)
values (1, 1, 2, 'Acceso limitado a cursos', 150.00, 'Beneficios...', current_date, '2021-12-31', true, current_date, current_date);

insert into t_subscription (id_subscription, id_subscription_type, id_user, description, price, benefits, subscription_start_date,
                            subscription_end_date, status, created_at, updated_at)
values (2, 3, 1, 'Acceso a todos los cursos', 750.00, 'Beneficios...', '2021-06-10', '2022-06-10', true, current_date, current_date);

insert into t_payment_detail (id_payment_detail, id_payment_method, id_currency, identity_card, cardholder_name, card_number,
    token_transaction, status_code, transaction_timestamp, amount, expiry_date, security_code, status, created_at, updated_at)
values (1, 1, 2, '71960340', 'Robert Huaman', '1111111111111', 'aaaaaaa', '200', '2020-06-24 19:41:08.700957-05', 400.00, '2022-09-01',
        '111', true, '2020-06-24', '2020-06-24');

insert into t_payment_detail (id_payment_detail, id_payment_method, id_currency, identity_card, cardholder_name, card_number,
    token_transaction, status_code, transaction_timestamp, amount, expiry_date, security_code, status, created_at, updated_at)
values (2, 1, 2, '71960340', 'Robert Huaman', '1111111111111', 'bbbbbbb', '200', '2021-06-10 19:41:08.700957-05', 750.00, '2022-09-01',
        '111', true, '2021-06-10', '2021-06-10');

insert into t_payment_detail (id_payment_detail, id_payment_method, id_currency, identity_card, cardholder_name, card_number,
    token_transaction, status_code, transaction_timestamp, amount, expiry_date, security_code, status, created_at, updated_at)
values (3, 1, 2, '71960333', 'Bryanne HC', '343434234343432', 'cccccc', '200', CURRENT_TIMESTAMP, 130.00, '2024-09-01',
        '111', true, current_date, current_date);


insert into t_event_type (id_event_type, description, status, created_at, updated_at)
values (1, 'MESES DE CORTESIA', true, current_date, current_date);

insert into t_event_type (id_event_type, description, status, created_at, updated_at)
values (2, 'PAUSA', true, current_date, current_date);

insert into t_event_type (id_event_type, description, status, created_at, updated_at)
values (3, 'CANCELACION', true, current_date, current_date);

insert into t_event_type (id_event_type, description, status, created_at, updated_at)
values (4, 'MEMBRESIA', true, current_date, current_date);

insert into t_subscription_event (id_subscription_event, id_payment_detail, id_subscription, id_subscription_type,
    id_event_type, event_timestamp, subscription_start_date, subscription_end_date, status, created_at, updated_at)
values (1, 1, 2, 1, 4, '2020-06-24 19:41:08.700957-05', '2020-06-24', '2020-07-24', true, '2020-06-24', '2020-06-24');

insert into t_subscription_event (id_subscription_event, id_payment_detail, id_subscription, id_subscription_type,
    id_event_type, event_timestamp, subscription_start_date, subscription_end_date, status, created_at, updated_at)
values (2, NULL, 2, 1, 1, '2020-07-24 19:41:08.700957-05', '2020-07-24', '2020-10-24', true, '2020-07-24', '2020-07-24');

insert into t_subscription_event (id_subscription_event, id_payment_detail, id_subscription, id_subscription_type,
    id_event_type, event_timestamp, subscription_start_date, subscription_end_date, status, created_at, updated_at)
values (3, NULL, 2, 1, 2, '2020-10-24 19:41:08.700957-05', '2020-10-24', '2021-06-24', true, '2020-10-24', '2020-10-24');

insert into t_subscription_event (id_subscription_event, id_payment_detail, id_subscription, id_subscription_type,
    id_event_type, event_timestamp, subscription_start_date, subscription_end_date, status, created_at, updated_at)
values (4, 2, 2, 3, 4, '2021-06-10 19:41:08.700957-05', '2021-06-10', '2022-06-10', true, '2021-06-10', '2021-06-10');

insert into t_subscription_event (id_subscription_event, id_payment_detail, id_subscription, id_subscription_type,
    id_event_type, event_timestamp, subscription_start_date, subscription_end_date, status, created_at, updated_at)
values (5, 3, 1, 1, 4, CURRENT_TIMESTAMP, current_date, '2021-12-31', true, current_date, current_date);

