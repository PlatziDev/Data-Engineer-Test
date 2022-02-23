# Descripcion de la prueba

En el equipo de platzi queremos evaluar tus capacidades en modelamiento de datos y manejo de ingeniería de datos y ETL con algún lenguaje en específico.

Para esto decidimos crear la siguiente prueba en la cual se evaluará tu lógica de abstracción del negocio a los datos y la creación de scripts para ETL.

## **Platzi**

En platzi, ofrecemos educación online efectiva a estudiantes de todo el mundo, el modelo de negocio funciona de la siguiente manera

- Un estudiante puede adquirir 3 tipos de suscripciones pagas
- Existen distintos métodos de pago que se clasifican en recurrente y no recurrente
- Un estudiante puede pagar su suscripción con mas de un método de pago, es importante saber cuánto se pago, en que currency y en que fecha
- Es importante saber cuando un estudiante inicia y termina su suscripción
- Un estudiante puede pausar su suscripción o se le pueden dar meses de cortesía, y es necesario saber cuándo ocurre cada evento de pausa o cortesía
- Un estudiante puede tomar cursos, escuelas y clases
- Una escuela está conformada por cursos, y un curso está conformado por clases
- Además un estudiante puede ingresar a sesiones en vivo o blogs de la plataforma

1. Crear un modelo relacional que pueda soportar la lógica de negocio anterior
2. Crear un modelo BI en estrella o snowflake para analitica de datos, para analizar los pagos en platzi y el dinero que se obtiene.
3. Consultas sql:

En tu modelo de datos:

- cómo podemos saber cuántos estudiantes nuevos tenemos por suscripción semana a semana y mes por mes
- ¿Cuántos cursos ha tomado el estudiante con más del 80% de las clases vistas?
- ¿El estudiante ha tenido pausas o cortesías en su suscripción?

4. Crea un proceso de ETL en python/spark/sql o el lenguaje que creas conveniente con el objetivo de migrar los datos del modelo relacional que creaste anteriormente hasta el modelo estrella o snowflake que también creaste previamente.

Nota: Puedes asumir que el datawarehouse donde esta alojado el modelo de BI, es redshift, snowflake, hbase o cualquier base de datos columnar que manejes.

Formato de entrega:

Por favor hazle un fork al proyecto, cuando termines manda un PR con el siguiente formato interview/<your last name>, ejemplo: interview/vega y comunicate con el recluter o la persona que envió la prueba

Tienes una semana a partir de recibido este correo, muchos exitos.

Si tienes cualquier duda al respecto no dudes en escribirme.
