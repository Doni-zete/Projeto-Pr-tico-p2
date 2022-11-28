from flask import Flask, Blueprint, request, session, make_response,render_template,jsonify,redirect
from CRUD.crud import  criarBases,cadastrarCliente ,verificaLogin,meuBanco
# from flask_cors import CORS
from moedas.moedas import moedas_blueprint
from clientes.clientes import clientes_blueprint
app = Flask(__name__)
criarBases()

app.register_blueprint(moedas_blueprint)
app.register_blueprint(clientes_blueprint)



app.secret_key ="123hudsadasdw"

@app.route("/")
def Inicio():
  return render_template('tela_incial.html')




@app.route('/tela_cadatro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        informacao = request.form
        nome = informacao['nome']
        email = informacao['email']
        senha = informacao['senha']

        cur = meuBanco.cursor()
        cur.execute("INSERT INTO trabalhoP2_db.tabela_cliente(nome,email,senha) VALUES (%s, %s,%s)", (nome,email,senha))
        meuBanco.commit()
        cur.close()
        return redirect('/')
    return render_template('tela_cadatro.html')


@app.route("/tela_login")
def Login():
  return render_template('tela_login.html')


# @app.route("/tela_cadatro")
# def Cadastrar():
#   return render_template('tela_cadatro.html')



@app.route("/tela_menu")
def menu_aplicacao():
  return render_template('tela_menu.html')


# @app.route("/tela_listar_clientes")  
# def Listar_clientes():
#   return render_template("tela_listar_clientes.html")



@app.route('/tela_listar_clientes', methods=['GET','POST'])
def select():
    cursor = meuBanco.cursor()    
    sql = "SELECT *  FROM `trabalhoP2_db`.`tabela_cliente`"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_listar_clientes.html", content=results)



@app.route("/deletar", methods=['GET', 'POST'])
def deletar():
  cursor = meuBanco.cursor()
  sql = "DELETE FROM trabalhoP2_db.tabela_cliente WHERE id = %s"
  cursor.execute(sql,(request.args.get('id'),))
  meuBanco.commit()
  return redirect('/tela_listar_clientes')
 

     
# @app.route("/", methods=['GET', 'POST'])
# def hello_word():
#   if request.method == "GET":

#     if request.cookies.get("usuario"):
#       resp = make_response("Meu site com cookie setado.")
#     else:
#       resp = make_response("Meu site sem cookie.")
#       resp.set_cookie('usuario', 'doni')

#     cursor = meuBanco.cursor()
#     sql = "SELECT * FROM `trabalhoP2_db`.`tabela_cliente`"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     print(results)  
#     print("CONECTADO!")
#     return render_template("index.html",content=results)

#   else:
#     return "O que veio do meu form: "+request.form['conteudo']  







@app.route("/tela_inserir_cliente")  
def Inserir():
  return render_template("tela_inserir_cliente.html")  

# @app.route("/tela_listar_clientes")  
# def clientes(nome_cliente):
#   return render_template("tela_listar_clientes.html",nome_cliente=nome_cliente)






# ativando o debugar 
# if __name__ == "__name__":
# app.run(debug=True)

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

    


# @app.route("/", methods=['GET', 'POST'])
# def index():
#   cursor = meuBanco.cursor()
#   sql = "SELECT * FROM cliente"
#   cursor.execute(sql)
  
#   results = cursor.fetchall()
#   print(results)  
#   print("CONECTADO!")
#   return render_template("index.html",content=results)

@app.route("/tela_atualizar_clientes", methods=['GET', 'POST'])
def atualizar_cliente():
  if request.method == "POST":
      informacao = request.form
      nome = informacao['nome']
      email = informacao['email']
      senha = informacao['senha']

      cursor = meuBanco.cursor()
      sql = "UPDATE  trabalhoP2_db.tabela_cliente SET nome = %s, email = %s, senha = %s WHERE id = %s"
      cursor.execute(sql,(nome, email, senha, id))
      meuBanco.commit()


      # print(id)

      cursor = meuBanco.cursor()
      sql = "SELECT * FROM trabalhoP2_db.tabela_cliente"

      cursor.execute(sql)
      # meuBanco.commit()
      results = cursor.fetchall()
      print(results)  
      print("CONECTADO!")
      return render_template("tela_listar_clientes",content=results)

  else:
    cursor = meuBanco.cursor()
    sql = "SELECT * FROM trabalhoP2_db.tabela_cliente"
    cursor.execute(sql)

    results = cursor.fetchall()
    print(results)  
    print("CONECTADO!")
    return render_template("tela_atualizar_clientes.html",content=results)

 




# @app.route("/noticia/<noticia_slug>")
# def noticia(noticia_slug):
#   return "Noticia: "+noticia_slug

app.run(debug= True)