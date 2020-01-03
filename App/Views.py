import psycopg2
from app import app
from flask import render_template,request,redirect
from app.configuraciones import *

conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur= conn.cursor()

@app.route("/")

cur.execute("select * from productos")
for fila in cur:
   print(fila)
conexion1.close()
