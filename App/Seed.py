from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into Clientes (rut, nombre, edad, sexo ) values ('18549939 ','Este Men ','20','1');
insert into Clientes (rut, nombre, edad, sexo ) values ('19955361 ','Este Ban ','20','1');
insert into Clientes (rut, nombre, edad, sexo ) values ('11111111 ','Elsa Pato','24','0');
insert into Clientes (rut, nombre, edad, sexo ) values ('98765432 ','HEAVY MACHINE GUN ','33','1');
insert into Clientes (rut, nombre, edad, sexo ) values ('12345678 ','Gonzalo Caceres ','33','1');

"""
cur.execute(sql)

sql = """
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('1','1','Coca Cola','1500','Bebida');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('2','1','Pepsi','2500','Bebida');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('3','1','Fideos Carrozi','500','Alimento');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('4','1','Arroz Acuenta','700','Alimento');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('5','1','Ketchup','2500','Condimento');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('6','1','Mayonesa','1500','Condimento');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('7','1','Sopa Instantanea','1500','Alimento');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('8','1','Lavaloza','2500','Aseo');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('9','1','Antigrasa','3500','Aseo');
insert into Productos id_producto,id_tienda,nombre,valor,categoria) 
values ('10','1','Ron','2500','Bebida');
"""

cur.execute(sql)
sql = """
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','1','100');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','2','10');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','3','5');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','4','50');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','5','60');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','6','5');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','7','2');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','8','3');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','9','30');
insert into Inventario (id_inventario,id_producto, stock_actual) values ('1','10','4');



"""
cur.execute(sql)

sql = """
insert into Ingredientes(nombre) values ('Arroz');
insert into Ingredientes(nombre) values ('Zanahoria');
insert into Ingredientes(nombre) values ('Choclo');
insert into Ingredientes(nombre) values ('Huevo');
insert into Ingredientes(nombre) values ('Papas');  
insert into Ingredientes(nombre) values ('Pollo');
insert into Ingredientes(nombre) values ('Vacuno');
insert into Ingredientes(nombre) values ('Cerdo');
insert into Ingredientes(nombre) values ('Pavo');
insert into Ingredientes(nombre) values ('Queso'); 
insert into Ingredientes(nombre) values ('Aceite de oliva');
insert into Ingredientes(nombre) values ('Salsa');
insert into Ingredientes(nombre) values ('Tomate');
insert into Ingredientes(nombre) values ('Cebolla');
insert into Ingredientes(nombre) values ('Vino blanco');  
insert into Ingredientes(nombre) values ('Placa de lasaña');
insert into Ingredientes(nombre) values ('Ajo');
insert into Ingredientes(nombre) values ('Aji');
insert into Ingredientes(nombre) values ('Pimiento');
insert into Ingredientes(nombre) values ('Sal');  
insert into Ingredientes(nombre) values ('Azucar');
insert into Ingredientes(nombre) values ('Bizcocho de soletilla');
insert into Ingredientes(nombre) values ('Cafe');
insert into Ingredientes(nombre) values ('Chocolate');
insert into Ingredientes(nombre) values ('Cacao'); 
insert into Ingredientes(nombre) values ('Mantequilla');
insert into Ingredientes(nombre) values ('Esparragos');
insert into Ingredientes(nombre) values ('Caldo de verduras');
insert into Ingredientes(nombre) values ('Crema');
insert into Ingredientes(nombre) values ('Leche'); 
insert into Ingredientes(nombre) values ('Pimienta');
insert into Ingredientes(nombre) values ('Macaco');
insert into Ingredientes(nombre) values ('Oregano');
insert into Ingredientes(nombre) values ('Comino');
insert into Ingredientes(nombre) values ('Arvejas'); 
insert into Ingredientes(nombre) values ('Manzana');
insert into Ingredientes(nombre) values ('Canela');
insert into Ingredientes(nombre) values ('Harina');
insert into Ingredientes(nombre) values ('Bistec de lomo');

"""
cur.execute(sql)

sql = """
insert into Contienen (id_producto, id_ingrediente) values ('1','1');
insert into Contienen (id_producto, id_ingrediente) values ('1','6');
insert into Contienen (id_producto, id_ingrediente) values ('1','11');
insert into Contienen (id_producto, id_ingrediente) values ('1','17');
insert into Contienen (id_producto, id_ingrediente) values ('1','19');
insert into Contienen (id_producto, id_ingrediente) values ('1','20');
insert into Contienen (id_producto, id_ingrediente) values ('2','8');
insert into Contienen (id_producto, id_ingrediente) values ('2','11');
insert into Contienen (id_producto, id_ingrediente) values ('2','16');
insert into Contienen (id_producto, id_ingrediente) values ('2','15');
insert into Contienen (id_producto, id_ingrediente) values ('2','10');
insert into Contienen (id_producto, id_ingrediente) values ('2','20');
insert into Contienen (id_producto, id_ingrediente) values ('2','12');
insert into Contienen (id_producto, id_ingrediente) values ('2','13');
insert into Contienen (id_producto, id_ingrediente) values ('2','14');
insert into Contienen (id_producto, id_ingrediente) values ('3','21');
insert into Contienen (id_producto, id_ingrediente) values ('3','22');
insert into Contienen (id_producto, id_ingrediente) values ('3','23');
insert into Contienen (id_producto, id_ingrediente) values ('3','24');
insert into Contienen (id_producto, id_ingrediente) values ('3','25');
insert into Contienen (id_producto, id_ingrediente) values ('3','10');
insert into Contienen (id_producto, id_ingrediente) values ('3','4');
insert into Contienen (id_producto, id_ingrediente) values ('4','26');
insert into Contienen (id_producto, id_ingrediente) values ('4','27');
insert into Contienen (id_producto, id_ingrediente) values ('4','28');
insert into Contienen (id_producto, id_ingrediente) values ('4','29');
insert into Contienen (id_producto, id_ingrediente) values ('4','5');
insert into Contienen (id_producto, id_ingrediente) values ('4','20');
insert into Contienen (id_producto, id_ingrediente) values ('4','31');
insert into Contienen (id_producto, id_ingrediente) values ('4','16');
insert into Contienen (id_producto, id_ingrediente) values ('5','32');
insert into Contienen (id_producto, id_ingrediente) values ('5','17');
insert into Contienen (id_producto, id_ingrediente) values ('5','2');
insert into Contienen (id_producto, id_ingrediente) values ('5','15');
insert into Contienen (id_producto, id_ingrediente) values ('5','33');
insert into Contienen (id_producto, id_ingrediente) values ('5','34');
insert into Contienen (id_producto, id_ingrediente) values ('5','31');
insert into Contienen (id_producto, id_ingrediente) values ('5','20');
insert into Contienen (id_producto, id_ingrediente) values ('5','35');
insert into Contienen (id_producto, id_ingrediente) values ('6','36');
insert into Contienen (id_producto, id_ingrediente) values ('6','21');
insert into Contienen (id_producto, id_ingrediente) values ('6','37');
insert into Contienen (id_producto, id_ingrediente) values ('6','38');
insert into Contienen (id_producto, id_ingrediente) values ('6','20');
insert into Contienen (id_producto, id_ingrediente) values ('6','26');
insert into Contienen (id_producto, id_ingrediente) values ('6','4');
insert into Contienen (id_producto, id_ingrediente) values ('7','39');
insert into Contienen (id_producto, id_ingrediente) values ('7','39');
insert into Contienen (id_producto, id_ingrediente) values ('7','5');
insert into Contienen (id_producto, id_ingrediente) values ('7','16');
insert into Contienen (id_producto, id_ingrediente) values ('7','4');
insert into Contienen (id_producto, id_ingrediente) values ('7','1');
insert into Contienen (id_producto, id_ingrediente) values ('7','31');
insert into Contienen (id_producto, id_ingrediente) values ('7','20');


"""
cur.execute(sql)

sql = """
insert into Beben (id_bebestible, id_cliente, fecha,hora) 
values ('1','18549939',now() ,now());
insert into Beben (id_bebestible, id_cliente, fecha,hora) 
values ('14','19955361',now() ,now());
insert into Beben (id_bebestible, id_cliente, fecha,hora) 
values ('2','11111111',now() ,now());
insert into Beben (id_bebestible, id_cliente, fecha,hora) 
values ('14','98765432','10-10-2018' ,now());
insert into Beben (id_bebestible, id_cliente, fecha,hora) 
values ('14','98765432','04-04-2018' ,now());
"""
cur.execute(sql)

sql = """
insert into Consumen (id_producto, id_cliente, fecha, hora)
values ('3','18549939','05-05-2018',now());

insert into Consumen (id_producto, id_cliente, fecha, hora)
values ('4','12345678','04-04-2018',now());

insert into Consumen (id_producto, id_cliente, fecha, hora)
values ('5','19955361','08-07-2018',now());
insert into Consumen (id_producto, id_cliente, fecha, hora)
values ('6','19955361',now(),now());
insert into Consumen (id_producto, id_cliente, fecha, hora)
values ('7','11111111',now(),now());
insert into Consumen (id_producto, id_cliente, fecha, hora)
values ('7','98765432',now(),now());
"""
cur.execute(sql)


conn.commit()
cur.close()
conn.close()
