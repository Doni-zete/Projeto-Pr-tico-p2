from flask import Flask, redirect, render_template, request, session, make_response

from CRUD.crud import  criarBases,cadastrarCliente ,verificaLogin
# from flask_cors import CORS

app = Flask(__name__)
criarBases()


app.secret_key ="123hudsadasdw"



# @app.route('/cadastrarCliente', methods=['POST'])
# def cadastrarCliente():
#   cadastrarCliente(request.json)
#   print('VALOR Aqui {}'.format(request.json))
#   return jsonify(request.json)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   resu = verificaLogin(request.json)
#   print(resu)
#   # with open('log.txt', 'w') as outfile:
#   #   json.dump(resu, outfile)
#   # json.dump(resu, 'log')
#   return  resu if resu != None else "ERRO"

# @app.route('/cadastrarUsuario', methods=['POST'])
# def cadastraUsuario():
  
#   cadastraUsuario(request.json)
#   return 'sucesso'



  
@app.route("/", methods=['GET', 'POST'])
def INICIO():
  if request.method == "GET":
    return render_template("telaLogin.html",content=['nome','endereco'])
  else:
    return request.form['nome','endereco']  
    
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