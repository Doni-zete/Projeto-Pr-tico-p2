from flask import Flask, redirect, render_template, Blueprint, request, session, make_response
# from CRUD.crud import  criarBases,cadastrarCliente ,verificaLogin
# from flask_cors import CORS
from moedas.moedas import moedas_blueprint
from clientes.clientes import clientes_blueprint
app = Flask(__name__)
# criarBases()

app.register_blueprint(moedas_blueprint)
app.register_blueprint(clientes_blueprint)


app.secret_key ="123hudsadasdw"


# @app.route('/clientes')
# def listar_clientes():
#   return render_template('listar_clientes.html')

# @app.route('/moedas/<id>')
# def criar_client(id):
#   return render_template('criar_clientes.html')








  
# @app.route("/", methods=['GET', 'POST'])
# def INICIO():
#   if request.method == "GET":
#     return render_template("telaLogin.html",content=['username'])
#   else:
#     return request.form['username']  
    
    # if request.cookies.get("usuario"):
    #   resp = make_response("Meu site com cookie setado.")
    # else:
    #   resp = make_response("Meu site sem cookie.")
    #   resp.set_cookie('usuario', 'doni')

    # cursor = meuBanco.cursor()
    # sql = "SELECT * FROM cliente"
    # cursor.execute(sql)
    # results = cursor.fetchall()
    # print(results)  
    # print("CONECTADO!")
    
  # else:
  #   return "O que veio do meu form: "+request.form['conteudo']  


# @app.route("/")
# def login():
#   return render_template("telaLogin.html")

    
# @app.route("/deletar", methods=['GET', 'POST'])
# def deletar():
#   cursor = meuBanco.cursor()
#   sql = "DELETE FROM cliente WHERE id = %s"
#   cursor.execute(sql,(request.args.get('id'),))
#   meuBanco.commit()
#   return redirect("/")


# @app.route("/", methods=['GET', 'POST'])
# def index():
#   cursor = meuBanco.cursor()
#   sql = "SELECT * FROM cliente"
#   cursor.execute(sql)
  
#   results = cursor.fetchall()
#   print(results)  
#   print("CONECTADO!")
#   return render_template("index.html",content=results)

# @app.route("/atualizar", methods=['GET', 'POST'])
# def atualizar_cliente():
#   if request.method == 'POST':
#       id = request.form.get('id')
#       nome = request.form.get('nome')
#       endereço = request.form.get('endereço')
#       cursor = meuBanco.cursor()
#       sql = "UPDATE  cliente SET nome = %s,endereço = %s WHERE id = %s"


#       cursor.execute(sql,(nome, endereço, id))
#       meuBanco.commit()


#       # print(id)

#       cursor = meuBanco.cursor()
#       sql = "SELECT * FROM cliente"

#       cursor.execute(sql)
#       # meuBanco.commit()
#       results = cursor.fetchall()
#       print(results)  
#       print("CONECTADO!")
#       return render_template("index.html",content=results)

#   else:
#       cursor = meu_banco.cursor()
#       sql = "SELECT * FROM cliente"
#       cursor.execute(sql)
      
#       results = cursor.fetchall()
#       print(results)  
#       print("CONECTADO!")
#       return render_template("index.html",content=results)

 




# @app.route("/noticia/<noticia_slug>")
# def noticia(noticia_slug):
#   return "Noticia: "+noticia_slug