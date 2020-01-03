import psycopg2
from configuraciones import *

conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur= conn.cursor()

cur.execute("select productos.nombre from productos")
for fila in cur:
   print(fila)
conn.close()
