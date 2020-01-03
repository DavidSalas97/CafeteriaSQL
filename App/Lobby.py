import psycopg2

conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur= conn.cursor()

while true:
  print('Porfavor seleccione una opción:', '1. Productos sin stock actualmente','2. Información del dueño de la tienda',
  '3. Nombre y dirección de la tienda','4. Fechas donde se realizaron ventas y cuantas se realizaron',
  '5. Datos del cliente con más compras realizadas','6. Producto más caro','7. Producto menos vendido','8. Venta con el mayor monto total'
  ,'9. Producto más vendido segun cada categoria','10.Monto total de las ventas del mes de Diciembre',
  '11. Obtener un listado completo de los productos, y cuantas veces se a vendido cada uno.', '12.Ingresar consulta manualmente', sep='\n')


  A = input()
  if(A==1):
     cur.execute("SELECT productos.nombre FROM productos,inventario WHERE inventario.stock_actual=0;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==2):
       cur.execute("SELECT * FROM dueno;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==3):
       cur.execute("SELECT tiendas.nombre, tiendas.nombre_calle, tiendas.n_local FROM tiendas;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==4):
       cur.execute("SELECT count(*) FROM ventas GROUP BY ventas.fecha ORDER BY 2;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==5):
       cur.execute("SELECT * FROM clientes FROM (SELECT sum(ventas.id_venta) AS cuantos ,clientes.rut FROM clientes,ventas WHERE ventas.rut_cliente=clientes.rut GROUP BY clientes.rut) AS piden WHERE piden.cuantos=(SELECT max(x.cuantos) FROM (SELECT sum(ventas.id_ventas) AS cuantos) FROM clientes,ventas WHERE ventas.rut_cliente=clientes.rut GROUP BY clientes.rut) AS x;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==6):
       cur.execute("SELECT e.nombre FROM (SELECT productos.nombre,max(productos.precio) FROM productos) AS e;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==7):
       cur.execute("SELECT p.nombre FROM (SELECT productos.nombre,sum(compone.cantidad) AS cuantos FROM productos,compone WHERE productos.id_producto=compone.id_producto GROUP BY productos.nombre) AS p WHERE p.cuantos=(SELECT min(x.cuantos) FROM (SELECT sum(compone.cantidad) AS cuantos) FROM productos,compone WHERE productos.id_producto=compone.id_producto GROUP BY productos.nombre) AS x;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==8):
       cur.execute("SELECT e.id_venta FROM (SELECT ventas.id_venta, sum(compone.monto) AS total FROM ventas,compone WHERE ventas.id_venta=compone.id_venta GROUP BY ventas.id_venta) AS piden WHERE piden.total = (SELECT max(x.total) FROM (SELECT ventas.id_venta, sum (compone.monto) AS total FROM ventas,compone WHERE ventas.id_venta=compone.id_venta GROUP BY ventas.id_venta) AS x;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==9):
       cur.execute("SELECT productos.nombre, productos.categoria FROM (SELECT productos.nombre, productos.categoria, sum(compone.cantidad) AS total FROM productos,compone WHERE compone.id_producto=productos.id_producto GROUP BY productos.nombre) AS piden WHERE piden.total=(SELECT max(x.cuantos) FROM ( SELECT productos.nombre, productos.categoria, sum (componen.cantidad) AS total FROM productos,compone WHERE compone.id_producto=productos.id_producto GROUP BY productos.nombre) AS x")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==10):
       cur.execute("SELECT sum(compone.monto) FROM compone,ventas WHERE compone.id_venta=ventas.id_venta BETWEEN '20191201' AND '20191230';")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==11):
       cur.execute("SELECT productos.nombre, count(compone.cantidad) FROM productos,compone WHERE productos.id_producto=compone.id_producto;")
     for fila in cur:
       print(fila)
     conn.close()
  if(A==12):
       cur.execute("select productos.nombre from productos")
     for fila in cur:
       print(fila)
     conn.close()
  if(A>12 or A<1):
     print('Valor invalido)
