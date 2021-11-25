-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-- # 1. cómo podemos saber cuántos estudiantes nuevos tenemos por suscripción semana a semana
--      y mes a mes
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------

select
    date_part('year', event_timestamp) as year,
    date_part('week', event_timestamp) as period, -- para mes habría que cambiar a 'month'
    count(1) as count_new_students
from
(
	select
        e.event_timestamp,
        e.id_subscription,
        e.id_subscription_type,
        t.name as subscription_type_name,
        rank() over (partition by e.id_subscription, e.id_subscription_type order by event_timestamp)
	from
	    t_subscription_event e
	left join
	    t_subscription_type t
	on e.id_subscription_type = t.id_subscription_type
) subscription_events_new
where rank = 1
group by year, period, subscription_type_name
order by year desc;

-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-- # 2. ¿Cuántos cursos ha tomado el estudiante con más del 80% de las clases vistas?
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------

select
    student,
    count(1) courses_completed_more_than_80_per
from
(
	select
		u.first_name || ' ' ||  u.last_name as student,
		count(distinct c.id_class) count_classes_watched,
		count(distinct cl.id_class) count_class_per_course
	from
		t_enrollment_class ec
	inner join
		t_user u
	on u.id_user = ec.id_user
	left join
		t_class c
	on ec.id_class in (c.id_class)
	inner join
		t_course cc
	on cc.id_course = c.id_course
	left join
		t_class cl
	on cc.id_course in (cl.id_course)
	group by c.id_course, student
) watched_classes
where (count_classes_watched*100)/count_class_per_course > 80
group by student
order by courses_completed_more_than_80_per desc;

-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-- # 3. ¿El estudiante ha tenido pausas o cortesías en su suscripción?
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------

select
    u.first_name || ' ' ||  u.last_name as student,
    et.description as event_type,
    count(1) as times_occurred
from
    t_subscription_event se
inner join
    t_event_type et
on se.id_event_type = et.id_event_type
inner join
    t_subscription s
on s.id_subscription = se.id_subscription
inner join
    t_user u
on u.id_user = s.id_user
where se.id_event_type in (1, 2)
group by student, event_type;