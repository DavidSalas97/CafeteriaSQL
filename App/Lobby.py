import psycopg2
import subprocess as sp
from configuraciones import *
conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur= conn.cursor()
B=1
while B==1:
  conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))
  cur= conn.cursor()
  print('\n')
  print('Porfavor seleccione una opción:', '1. Productos sin stock actualmente','2. Información del dueño de la tienda',
  '3. Nombre y dirección de la tienda','4. Fechas donde se realizaron ventas y cuantas se realizaron',
  '5. Datos del cliente con más compras realizadas','6. Producto más caro','7. Producto menos vendido','8. Venta con el mayor monto total'
  ,'9. Producto más vendido y su categoria','10.Monto total de las ventas del mes de Diciembre',
  '11. Obtener un listado completo de los productos, y cuantas veces se a vendido cada uno.', '12.Ingresar consulta manualmente','13. Ingresar datos a la base de datos','14. Finalizar','\n', sep='\n')


  A = input()
  if(A=="1"):
    cur.execute("SELECT productos.nombre FROM productos,inventario WHERE inventario.stock_actual=0 AND productos.id_producto=inventario.id_producto;")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="2"):
    cur.execute("SELECT * FROM dueño;")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="3"):
    cur.execute("SELECT tiendas.nombre, tiendas.nombre_calle, tiendas.n_local FROM tiendas;")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="4"):
    cur.execute("SELECT count(*),ventas.fecha FROM ventas GROUP BY ventas.fecha;")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="5"):
    cur.execute("SELECT * from clientes,(select count(ventas.id_venta) as veces, clientes.rut from ventas,clientes where clientes.rut=ventas.rut_cliente group by clientes.rut) as total where clientes.rut=total.rut and total.veces = (select max(x.veces) from (select count(ventas.id_venta) as veces,ventas.rut_cliente from ventas group by ventas.rut_cliente) as x);")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="6"):
    cur.execute("SELECT productos.nombre FROM productos where productos.valor=(SELECT max(productos.valor) FROM productos);")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="7"):
    cur.execute("SELECT p.nombre FROM (SELECT productos.nombre,sum(compone.cantidad) AS cuantos FROM productos,compone WHERE productos.id_producto=compone.id_producto GROUP BY productos.nombre) AS p WHERE p.cuantos=(SELECT min(x.cuantos) FROM (SELECT sum(compone.cantidad) AS cuantos from productos,compone WHERE productos.id_producto=compone.id_producto GROUP BY productos.nombre) AS x);")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="8"):
    cur.execute("SELECT ventas.id_venta FROM (SELECT ventas.id_venta, sum(compone.monto) AS total FROM ventas,compone WHERE ventas.id_venta=compone.id_venta GROUP BY ventas.id_venta) AS piden, ventas WHERE piden.id_venta=ventas.id_venta and piden.total = (SELECT max(x.total) FROM (SELECT ventas.id_venta, sum (compone.monto) AS total FROM ventas,compone WHERE ventas.id_venta=compone.id_venta GROUP BY ventas.id_venta) AS x);")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="9"):
    cur.execute("SELECT productos.nombre, productos.categoria FROM (SELECT productos.id_producto,productos.nombre, productos.categoria, sum(compone.cantidad) AS total FROM productos,compone WHERE compone.id_producto=productos.id_producto GROUP BY productos.nombre, productos.categoria,productos.id_producto) AS piden,productos WHERE piden.id_producto=productos.id_producto and piden.total=(SELECT max(x.total) FROM ( SELECT productos.nombre,productos.categoria,sum(compone.cantidad) AS total FROM productos,compone WHERE compone.id_producto=productos.id_producto group by productos.nombre,productos.categoria) AS x);")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="10"):
    cur.execute("SELECT sum(compone.monto) from compone,ventas where compone.id_venta=ventas.id_venta and ventas.fecha between '20191201' and '20191230';")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=="11"):
    cur.execute("SELECT productos.nombre, sum(compone.cantidad) FROM productos,compone WHERE productos.id_producto=compone.id_producto group by productos.nombre;")
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=='12'):
    print("Escribe la sentencia a realizar", '\n')
    C=input()
    cur.execute(C)
    for fila in cur:
      print(fila)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=='13'):
    print("Escriba los datos para agregar", '\n')
    c=input()
    cur.execute(c)
    conn.commit()
    cur.close()
    conn.close()
  elif(A=='14'):
    break
  else:
    print("Valor inválido, seleccione otra opción", '\n')
  Z=input()
  tmp = sp.call('cls',shell=True)
