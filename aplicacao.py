from flask import Flask, redirect, render_template, request, session, make_response

from CRUD.crud import  criarBases
from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
criarBases()

app.secret_key ="123hudsadasdw"



  
# @app.route("/", methods=['GET', 'POST'])
# def hello_word():
#   if request.method == "GET":
    
#     if request.cookies.get("usuario"):
#       resp = make_response("Meu site com cookie setado.")
#     else:
#       resp = make_response("Meu site sem cookie.")
#       resp.set_cookie('usuario', 'doni')

#     cursor = db.cursor()
#     sql = "SELECT * FROM cliente"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     print(results)  
#     print("CONECTADO!")
#     return render_template("index.html",content=results)
    
#   else:
#     return "O que veio do meu form: "+request.form['conteudo']  


# @app.route("/")
# def login():
#   return render_template("telaLogin.html")

    
# @app.route("/deletar", methods=['GET', 'POST'])
# def deletar():
#   cursor = db.cursor()
#   sql = "DELETE FROM cliente WHERE id = %s"
#   cursor.execute(sql,(request.args.get('id'),))
#   db.commit()
#   return redirect("/")


# # @app.route("/", methods=['GET', 'POST'])
# # def index():
# #   cursor = db.cursor()
# #   sql = "SELECT * FROM cliente"
# #   cursor.execute(sql)
  
# #   results = cursor.fetchall()
# #   print(results)  
# #   print("CONECTADO!")
# #   return render_template("index.html",content=results)

# @app.route("/atualizar", methods=['GET', 'POST'])
# def atualizar_cliente():
#   if request.method == 'POST':
#       id = request.form.get('id')
#       nome = request.form.get('nome')
#       endereço = request.form.get('endereço')
#       cursor = db.cursor()
#       sql = "UPDATE  cliente SET nome = %s,endereço = %s WHERE id = %s"


#       cursor.execute(sql,(nome, endereço, id))
#       db.commit()


#       # print(id)

#       cursor = db.cursor()
#       sql = "SELECT * FROM cliente"

#       cursor.execute(sql)
#       # db.commit()
#       results = cursor.fetchall()
#       print(results)  
#       print("CONECTADO!")
#       return render_template("index.html",content=results)

#   else:
#       cursor = db.cursor()
#       sql = "SELECT * FROM cliente"
#       cursor.execute(sql)
      
#       results = cursor.fetchall()
#       print(results)  
#       print("CONECTADO!")
#       return render_template("index.html",content=results)

 




# @app.route("/noticia/<noticia_slug>")
# def noticia(noticia_slug):
#   return "Noticia: "+noticia_slug