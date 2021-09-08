with t2 as
(select *,
substring(fecha_inicio,1,4) as anio,
substring(fecha_inicio,6,2) as mes,
substring(fecha_inicio,9,2) as dia
from platzi_estu_entrerga.clases_estudiantes 
order by fecha_inicio desc),
t3 as(
select count(mes) as mes_suscripcion, mes
from t2
group by mes)
select * from t3
order by mes desc
limit 1;