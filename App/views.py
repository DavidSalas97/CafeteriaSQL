import psycopg2
from app import app
from flask import render_template,request,redirect
from app.configuraciones import *

conn=psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s"%(database,user,password,host,port))

cur= conn.cursor()

@app.route("/")


def index():
	sql="""
	select productos.nombre from productos,inventario where inventario.stock_actual=0;"""
	cur.execute(sql)

@app.route("/hola")
def hola():
	return "Hola."

#ruta dinamica	
@app.route("/user/<string:user>")
def user(user):
	return "hola" + user
@app.route("/numero/<int:n>")
def numero(n):
	return "Numero: {}".format(n)
@app.route("/user/<int:id>/<string:username>")
def username(id,username):
	return "ID: {},Nombre de usuario: {}".format(id, username)
