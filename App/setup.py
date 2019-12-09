from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname='tienda' user='postgres' password='postgres'")


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE Clientes
(id serial PRIMARY KEY, nombre varchar(255), edad int,
celular int,correo varchar(255));
"""
cur.execute(sql)

sql = """
CREATE TABLE Productos
(id serial PRIMARY KEY,
id_tienda int,
nombre varchar(40),
valor int,
categoria varchar(40));
"""
cur.execute(sql)

sql = """

CREATE TABLE Inventario
id serial PRIMARY KEY,
id_producto int,
stock_actual int);
"""
cur.execute(sql)

sql = """
CREATE TABLE Compone
(id_Producto serial PRIMARY KEY,
id_venta PRIMARY KEY,
cantidad int,
monto int);

"""
cur.execute(sql)

sql = """
CREATE TABLE Tiendas
(id serial PRIMARY KEY,
nombre varchar(40) ,
nombre_calle varchar(255),
n_local int);
"""
cur.execute(sql)

sql = """
CREATE TABLE Ventas
(id serial PRIMARY KEY,
rut_cliente varchar(40) ,
id_tienda int,
fecha date);
"""
cur.execute(sql)

sql = """
CREATE TABLE Dueño
(id serial PRIMARY KEY,
id_tienda int,
rut varchar(40),
nombre varchar(255),
celular int);
"""

cur.execute(sql)



conn.commit()
cur.close()
conn.close()
