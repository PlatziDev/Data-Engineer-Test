with conteo1 as (
select 
t1.idcursos_academicos,t2.idestudiantes
 from platzi_estu_entrerga.clases as t1
left join platzi_estu_entrerga.clases_estudiantes as t2
on 
t1.idclases=t2.idclases),
t4 as(
SELECT idestudiantes,idcursos_academicos,count(idestudiantes) as conteo_clases
FROM conteo1
group by idcursos_academicos,idestudiantes),
t5 as(
select idcursos_academicos,count(idcursos_academicos) as conteo_ac
from platzi_estu_entrerga.clases
group by idcursos_academicos,idcursos_academicos),
t6 as (
select t4.idestudiantes,t4.conteo_clases,t5.conteo_ac
from t4 inner join t5
on t5.idcursos_academicos=t4.idcursos_academicos
where t4.conteo_clases<> 0),
t7 as(
select 
idestudiantes,conteo_clases,conteo_ac,
round(conteo_clases * 100 / conteo_ac,0)  as porcentaje 
from t6
order by idestudiantes)
select * from t7
where porcentaje >=80