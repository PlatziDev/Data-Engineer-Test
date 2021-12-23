--cómo podemos saber cuántos estudiantes nuevos tenemos por suscripción semana a semana y mes por mes
--per year
select
       DATE_PART('week', created_at) AS week_number,
       DATE_PART('yr', created_at) AS yr,
       count(1) as n_records
from subscription_states
group by 1,2
--per month
select
       DATE_PART('month', created_at) AS _month,
       DATE_PART('yr', created_at) AS yr,
       count(1) as n_records
from subscription_states
group by 1,2

--¿Cuántos cursos ha tomado el estudiante con más del 80% de las clases vistas?

select
       s.student_id,
       s.full_name,
       count(1) as n_courses
from students_courses s_co
inner join
     students s on s.student_id = s_co.student_id
inner join
    students_classes sc on s.student_id = sc.student_id
inner join
    classes cl on sc.class_id = cl.class_id
and s_co.course_id = cl.course_id
where sc.percentage_completed > 80
group by 1,2

--¿El estudiante ha tenido pausas o cortesías en su suscripción?
select
       s.student_id,
       s.full_name,
       ss.subscription_type,
       count(*)
from students s
inner join
    subscription_states ss on s.student_id = ss.student_id
where ss.subscription_type in ('PAUSED', 'GIFT')
group by 1,2,3