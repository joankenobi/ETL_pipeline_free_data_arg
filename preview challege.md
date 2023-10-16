
# 1 Challenge Data Analytics - Python 🚀
¡Te damos la bienvenida al Challenge de Data Analytics con Python! de la empresa ALKEMI

En este documento podrás ver todos los detalles del proyecto que deberás realizar
para ingresar a la aceleración.

¿Estás list@? ¡Empecemos! 🏁

## Objetivo 👈
Para resolver este challenge, deberás crear un proyecto que *consuma datos* desde
3 fuentes distintas para *popular una base de datos SQL* con información cultural
sobre bibliotecas, museos y salas de cines argentinos.

# Requerimientos funcionales 🔎
Tu proyecto deberá cumplir con una serie de requerimientos funcionales que giran
en torno a cuatro ejes centrales: 
- los archivos fuente, 
- el procesamiento de datos, 
- la creación de tablas en la base de datos y 
- la actualización de la base de datos.
Veamos cada uno de ellos en detalle.

## 1 Archivos fuente
Los archivos fuentes serán utilizados en tu proyecto para obtener de ellos todo lo
necesario para *popular la base de datos*. El proyecto deberá:
- Obtener los 3 archivos de fuente utilizando la *librería requests* y
almacenarse en *forma local* (Ten en cuenta que las urls pueden cambiar en
un futuro):

- Datos Argentina - [Museos](https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d)
- Datos Argentina - [Salas de Cine](https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_f7a8edb8-9208-41b0-8f19-d72811dcea97)
- Datos Argentina - [Bibliotecas Populares](https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7)

Organizar los archivos en rutas siguiendo la siguiente estructura:
“categoría\año-mes\categoria-dia-mes-año.csv”
- Por ejemplo: “museos\2021-noviembre\museos-03-11-2021”
- Si el archivo existe debe reemplazarse. La fecha de la nomenclatura es la fecha de descarga.

## 2 Procesamiento de datos
El procesamiento de datos permitirá a nuestro proyecto transformar los datos de los
archivos fuente en la información que va a *nutrir la base de datos*. Para esto, el
proyecto deberá:
- Normalizar toda la información de Museos, Salas de Cine y Bibliotecas
Populares, *para crear una única tabla que contenga*:
- - cod_localidad
- - id_provincia
- - id_departamento
- - categoría
- - provincia
- - localidad
- - nombre
- - domicilio
- - código postal
- - número de teléfono
- - mail
- - web

- Procesar los datos conjuntos para poder generar una tabla con la siguiente
información:
- - Cantidad de registros totales por categoría
- - Cantidad de registros totales por fuente
- - Cantidad de registros por provincia y categoría

- Procesar la información de cines para poder crear una tabla que contenga:
- - Provincia
- - Cantidad de pantallas
- - Cantidad de butacas
- - Cantidad de espacios INCAA

## 3 Creación de tablas en la Base de datos
Para disponibilizar la información obtenida y procesada en los pasos previos, tu proyecto deberá tener una base de datos que cumpla con los siguientes requisitos:
- La base de datos debe ser *PostgreSQL*
- Se deben crear los *scripts .sql* para la *creación de las tablas.*
- Se debe crear un *script .py* que ejecute los *scripts .sql* para *facilitar el deploy*.
- Los datos de la *conexión* deben poder configurarse fácilmente para facilitar el deploy en un nuevo ambiente de ser necesario.

## Actualización de la base de datos
Luego de normalizar la información y generar las demás tablas, las mismas se deben actualizar en la base de datos. Para eso, es importante tener en cuenta que:
- Todos los registros existentes deben ser reemplazados por la nueva
información.
- Dentro de cada tabla debe indicarse en una columna adicional la fecha de
carga.
