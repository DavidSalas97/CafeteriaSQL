import psycopg2
from configuraciones import *
conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur = conn.cursor()

sql ="""
insert into Clientes (id_cliente, nombre, edad, celular, correo) 
values ('18549939 ','Juan ','20','96453584','falso321@hotmail.com');
insert into Clientes (id_cliente, nombre, edad, celular, correo) 
values ('20654324 ','Gonzalo ','25','94135975','falso123@hotmail.com');
insert into Clientes (id_cliente, nombre, edad, celular, correo) 
values ('24022365 ','Maria ','21','96519871','falso856@hotmail.com');
insert into Clientes (id_cliente, nombre, edad, celular, correo) 
values ('19156701 ','Mario ','23','95417943','falso973@hotmail.com');
insert into Clientes (id_cliente, nombre, edad, celular, correo) 
values ('23214975 ','Julieta ','19','93216547','falso751@hotmail.com');
"""
cur.execute(sql)

sql = """
insert into Dueño (id_dueño, id_tienda, rut, nombre, celular)
values ('1','1','25483123','Patricio','96571236');
"""

cur.execute(sql)

sql = """
insert into Ventas (id_venta, rut_cliente, id_tienda, fecha) 
values ('1','18549939','1','20191205');
insert into Ventas (id_venta, rut_cliente, id_tienda, fecha) 
values ('2','20654324','1','20190925');
insert into Ventas (id_venta, rut_cliente, id_tienda, fecha) 
values ('3','24022365','1','20191223');
insert into Ventas (id_venta, rut_cliente, id_tienda, fecha) 
values ('4','19156701','1','20191115');
insert into Ventas (id_venta, rut_cliente, id_tienda, fecha) 
values ('5','23214975','1','20191201');
"""
cur.execute(sql)

sql = """
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('1','1','Coca Cola','1500','Bebida');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('2','1','Pepsi','2800','Bebida');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('3','1','Fideos Carrozi','500','Alimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('4','1','Arroz Acuenta','700','Alimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('5','1','Ketchup','2700','Condimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('6','1','Mayonesa','1600','Condimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('7','1','Sopa Instantanea','1200','Alimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('8','1','Lavaloza','2550','Aseo');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('9','1','Antigrasa','3500','Aseo');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('10','1','Ron','2500','Bebida');
"""
cur.execute(sql)

sql = """
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','1','100');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('2','2','10');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('3','3','5');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('4','4','50');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('5','5','60');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('6','6','5');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('7','7','2');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('8','8','3');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('9','9','30');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('10','10','4');
"""
cur.execute(sql)

sql = """
insert into Tiendas (id_tienda, nombre, nombre_calle, n_local)
values ('1','Elparo','Ejercito_Libertador','201');
"""
cur.execute(sql)

sql = """
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('1','1','2','3000');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('2','1','1','2500');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('4','1','4','2800');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('5','1','1','2500');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('1','2','4','6000');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('8','2','3','2500');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('6','2','2','3000');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('2','2','2','4500');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('4','2','3','2100');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('9','3','1','3500');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('8','3','1','2500');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('7','3','4','6000');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('6','3','6','6000');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('3','4','7','4500');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('2','4','2','500');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('4','4','1','700');
insert into Compone (id_producto, id_venta, cantidad, monto)
values ('1','4','1','1500');
insert into Compone (id_producto, id_venta, cantidad, monto) 
values ('10','5','5','12500');
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()