import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '1234' 
DB_NAME = 'platzi_estu_entrerga'
DB_NAME = 'modelo_bi'

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 

    return data


# drop registros de las tablas 
query = "delete from modelo_bi.estudiante_suscipcion"
result = run_query(query) 
print (result)

query = "delete from modelo_bi.metodos_de_pago "
result = run_query(query) 
print (result)

query = "delete from modelo_bi.estudiantes "
result = run_query(query) 
print (result)

query = "delete from modelo_bi.suscripcion "
result = run_query(query) 
print (result)

# autoincremental 
query = "ALTER TABLE modelo_bi.estudiante_suscipcion AUTO_INCREMENT=1"
result = run_query(query) 
print (result)

query = "ALTER TABLE modelo_bi.metodos_de_pago AUTO_INCREMENT=1"
result = run_query(query) 
print (result)

query = "ALTER TABLE modelo_bi.suscripcion AUTO_INCREMENT=1"
result = run_query(query) 
print (result)

query = "ALTER TABLE modelo_bi.estudiantes AUTO_INCREMENT=1"
result = run_query(query) 
print (result)

# insertan datos

query = "INSERT INTO modelo_bi.metodos_de_pago(descripcion) SELECT distinct descripcion FROM platzi_estu_entrerga.metodos_de_pago"
result = run_query(query) 
print (result)


query = "INSERT INTO modelo_bi.suscripcion(nombre,costo) SELECT distinct  nombre,costo FROM platzi_estu_entrerga.suscripcion"
result = run_query(query) 
print (result)


query = "INSERT INTO modelo_bi.estudiantes(documento,nombres,apellido,currency,recurrente,idsuscripcion) SELECT distinct documento,nombres,apellido,currency,recurrente,idsuscripcion FROM platzi_estu_entrerga.estudiantes"
result = run_query(query) 
print (result)


query = "INSERT INTO modelo_bi.estudiante_suscipcion(idestudiante_suscipcion,anio,mes,dia)SELECT distinct idestudiante_suscripcion,substring(fecha_suscripcion,1,4) as anio,substring(fecha_suscripcion,6,2) as mes,substring(fecha_suscripcion,9,2) as dia FROM platzi_estu_entrerga.estudiante_suscripcion"
result = run_query(query) 
print (result)

