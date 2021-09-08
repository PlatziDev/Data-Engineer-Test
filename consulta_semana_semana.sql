with t2 as
(
SELECT week(fecha_inicio) as semana
,fecha_inicio
FROM platzi_estu_entrerga.clases_estudiantes
order by fecha_inicio)
select count(semana) as cantidad_inscripcion, semana 
from t2
group by(semana)
limit 1;
