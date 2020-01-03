import psycopg2
from configuraciones import *
conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE Clientes
(rut serial PRIMARY KEY, 
nombre varchar(255), 
edad int,
celular int,
correo varchar(255));
"""
cur.execute(sql)

sql = """
CREATE TABLE Productos
(id_producto serial PRIMARY KEY,
id_tienda int,
nombre varchar(40),
valor int,
categoria varchar(40));
"""
cur.execute(sql)

sql = """

CREATE TABLE Inventario
(id_inventario serial PRIMARY KEY NOT NULL,
id_producto int,
stock_actual int);
"""
cur.execute(sql)

sql = """
CREATE TABLE Tiendas
(id_tienda serial PRIMARY KEY,
nombre varchar(40) ,
nombre_calle varchar(255),
n_local int);
"""
cur.execute(sql)

sql = """
CREATE TABLE Ventas
(id_venta serial PRIMARY KEY,
rut_cliente int,
id_tienda int,
fecha date);
"""
cur.execute(sql)

sql = """
CREATE TABLE Dueño
(id_dueño serial PRIMARY KEY,
id_tienda int,
rut varchar(40),
nombre varchar(255),
celular int);
"""
cur.execute(sql)

sql = """
CREATE TABLE Compone
(id_producto serial not null,
id_venta serial not null,
cantidad int not null,
monto int not null,
CONSTRAINT fk_producto FOREIGN KEY (id_producto) REFERENCES Productos (id_producto),
CONSTRAINT fk_venta FOREIGN KEY (id_venta) REFERENCES Ventas (id_venta));
"""
cur.execute(sql)


conn.commit()
cur.close()
conn.close()
