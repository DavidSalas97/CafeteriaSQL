from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into Clientes (id, nombre, edad, celular, correo) 
values ('18549939 ','Juan ','20','96453584','falso321@hotmail.com');
insert into Clientes (id, nombre, edad, celular, correo) 
values ('20654324 ','Gonzalo ','25','94135975','falso123@hotmail.com');
insert into Clientes (id, nombre, edad, celular, correo) 
values ('24022365 ','Maria ','21','96519871','falso856@hotmail.com');
insert into Clientes (id, nombre, edad, celular, correo) 
values ('19156701 ','Mario ','23','95417943','falso973@hotmail.com');
insert into Clientes (id, nombre, edad, celular, correo) 
values ('23214975 ','Julieta ','19','93216547','falso751@hotmail.com');

"""
cur.execute(sql)

sql = """
insert into Dueño (id, id_tienda, rut, nombre, celular)
values ('1','1','25483123','Patricio','96571236');
"""

cur.execute(sql)

sql = """
insert into Ventas (id, rut_cliente, id_tienda, fecha) 
values ('1','18549939','1',now());
insert into Ventas (id, rut_cliente, id_tienda, fecha) 
values ('2','20654324','1',now());
insert into Ventas (id, rut_cliente, id_tienda, fecha) 
values ('3','24022365','1',now());
insert into Ventas (id, rut_cliente, id_tienda, fecha) 
values ('4','19156701','1',now());
insert into Ventas (id, rut_cliente, id_tienda, fecha) 
values ('5','23214975','1',now());


"""
cur.execute(sql)

sql = """
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('1','1','Coca Cola','1500','Bebida');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('2','1','Pepsi','2500','Bebida');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('3','1','Fideos Carrozi','500','Alimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('4','1','Arroz Acuenta','700','Alimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('5','1','Ketchup','2500','Condimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('6','1','Mayonesa','1500','Condimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('7','1','Sopa Instantanea','1500','Alimento');
insert into Productos (id_producto,id_tienda,nombre,valor,categoria) 
values ('8','1','Lavaloza','2500','Aseo');
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
values ('1','2','10');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','3','5');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','4','50');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','5','60');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','6','5');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','7','2');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','8','3');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','9','30');
insert into Inventario (id_inventario,id_producto, stock_actual)
values ('1','10','4');

"""
cur.execute(sql)

sql = """
insert into Tiendas (id, nombre, nombre_calle, n_local)
values ('1','Elparo','Ejercito_Libertador','201');
"""
cur.execute(sql)


conn.commit()
cur.close()
conn.close()
