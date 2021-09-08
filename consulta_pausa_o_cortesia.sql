SELECT 
t3.idestudiantes,
t2.descripcion,
t3.documento,
t3.nombres,
t3.apellido,
t3.correo,
t3.telefono
FROM platzi_estu_entrerga.estados_estudiantes as t1
left join platzi_estu_entrerga.estado as t2
on t1.idestados_estudiantes=t2.idestados_estudiantes
left join platzi_estu_entrerga.estudiantes as t3
on t1.idestudiantes=t3.idestudiantes
where t2.descripcion in ('pausa','cortesia')