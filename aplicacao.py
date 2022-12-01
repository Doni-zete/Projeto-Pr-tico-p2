from flask import Flask, Blueprint, request, session, make_response,render_template,jsonify,redirect
from CRUD.crud import  criarBases,cadastrarCliente ,verificaLogin,meuBanco
# from flask_cors import CORS
app = Flask(__name__)
criarBases()




app.secret_key ="123hudsadasdw"

@app.route("/")
def Inicio():
  return render_template('tela_incial.html')


@app.route('/tela_cadatro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        informacao = request.form
        nome = informacao['nome']
        senha = informacao['senha']
        email = informacao['email']

        cur = meuBanco.cursor()
        cur.execute("INSERT INTO trabalhoP2_db.tabela_cliente(nome,email,senha) VALUES (%s, %s,%s)", (nome,email,senha))
        meuBanco.commit()
        cur.close()
        return redirect('/')
    return render_template('tela_cadatro.html')


@app.route("/tela_login")
def Login():
  return render_template('tela_login.html')


@app.route("/tela_menu")
def menu_aplicacao():
  return render_template('tela_menu.html')


@app.route('/tela_listar_clientes', methods=['GET','POST'])
def listar_cliente():
    cursor = meuBanco.cursor()    
    sql = "SELECT *  FROM `trabalhoP2_db`.`tabela_cliente`"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_listar_clientes.html", content=results)

@app.route('/tela_atualizar_clientes_dois', methods=['GET','POST'])
def atualizar_clientes_dois():
    cursor = meuBanco.cursor()    
    sql = "SELECT *  FROM `trabalhoP2_db`.`tabela_cliente`"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_atualizar_clientes_dois.html", content=results)


@app.route("/deletar_cliente", methods=['GET', 'POST'])
def deletar():
  cursor = meuBanco.cursor()
  sql = "DELETE FROM trabalhoP2_db.tabela_cliente WHERE id = %s"
  cursor.execute(sql,(request.args.get('id'),))
  meuBanco.commit()
  return redirect('/tela_listar_clientes')
 

@app.route("/tela_inserir_cliente",methods=['GET', 'POST'])  
def inserir_cliente():
  if request.method == "POST":
      informacao = request.form
      nome = informacao['nome']
      senha = informacao['senha']
      email = informacao['email']

      cur = meuBanco.cursor()
      cur.execute("INSERT INTO trabalhoP2_db.tabela_cliente(nome,email,senha) VALUES (%s, %s,%s)", (nome,email,senha))
      meuBanco.commit()
      cur.close()
      return redirect('/tela_inserir_cliente')
  return render_template('tela_inserir_cliente.html')


@app.route("/tela_atualizar_clientes", methods=['GET', 'POST'])
def atualizar_cliente():
  if request.method == "POST":
      informacao = request.form
      id = informacao['id']
      nome = informacao['nome']
      senha = informacao['senha']
      email = informacao['email']
      

      cursor = meuBanco.cursor()
      sql = "UPDATE  trabalhoP2_db.tabela_cliente SET nome = %s,senha = %s, email = %s  WHERE id = %s"
      cursor.execute(sql,(nome,senha, email,  id))
      meuBanco.commit()

      cursor = meuBanco.cursor()
      sql = "SELECT * FROM trabalhoP2_db.tabela_cliente WHERE id = %s "
      cursor.execute(sql,(request.args.get('id'),))

      
      # cursor.execute(sql)
      # meuBanco.commit()
      results = cursor.fetchall()
      print(results)  
      print("CONECTADO!")
      return render_template("tela_atualizar_clientes.html",content=results)

  else:
    cursor = meuBanco.cursor()
    sql = "SELECT * FROM trabalhoP2_db.tabela_cliente WHERE id = %s"
    # cursor.execute(sql)
    cursor.execute(sql,(request.args.get('id'),))

    results = cursor.fetchall()
    print(results)  
    print("CONECTADO!")
    return render_template("tela_atualizar_clientes.html",content=results)



@app.route('/tela_listar_moedas', methods=['GET','POST'])
def listar_moedas():
    cursor = meuBanco.cursor()    
    sql = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_listar_moedas.html", content=results)    


@app.route("/tela_inserir_moeda",methods=['GET', 'POST'])  
def inserir_moeda():
  if request.method == "POST":
      informacao = request.form
      moeda = informacao['moeda']
      simbolo = informacao['simbolo']
      valor = informacao['valor']
      quantidade = informacao['quantidade']


      cur = meuBanco.cursor()
      cur.execute("INSERT INTO trabalhoP2_db.tabela_moeda(moeda,simbolo,valor,quantidade) VALUES (%s, %s,%s,%s)", (moeda,simbolo,valor,quantidade))
      meuBanco.commit()
      cur.close()
      return redirect('/tela_inserir_moeda')
  return render_template('tela_inserir_moeda.html')    


@app.route("/deletar_moeda", methods=['GET', 'POST'])
def deletar_moeda():
  cursor = meuBanco.cursor()
  sql = "DELETE FROM trabalhoP2_db.tabela_moeda WHERE id = %s"
  cursor.execute(sql,(request.args.get('id'),))
  meuBanco.commit()
  return redirect('/tela_listar_moedas')
 


@app.route("/tela_atualizar_moedas", methods=['GET', 'POST'])
def atualizar_moeda():
  if request.method == "POST":
      informacao = request.form
      id = informacao['id']
      moeda = informacao['moeda']
      simbolo = informacao['simbolo']
      valor = informacao['valor']
      quantidade = informacao['quantidade']

      cursor = meuBanco.cursor()
      sql = "UPDATE  trabalhoP2_db.tabela_moeda SET moeda = %s, simbolo = %s, valor = %s, quantidade = %s WHERE id = %s"
      cursor.execute(sql,(moeda, simbolo, valor, quantidade,  id))
      meuBanco.commit()

      cursor = meuBanco.cursor()
      sql = "SELECT * FROM trabalhoP2_db.tabela_moeda WHERE id = %s "
      cursor.execute(sql,(request.args.get('id'),))

      
      # cursor.execute(sql)
      # meuBanco.commit()
      results = cursor.fetchall()
      print(results)  
      print("CONECTADO!")
      return render_template("tela_atualizar_moedas.html",content=results)

  else:
    cursor = meuBanco.cursor()
    sql = "SELECT * FROM trabalhoP2_db.tabela_moeda WHERE id = %s"
    # cursor.execute(sql)
    cursor.execute(sql,(request.args.get('id'),))

    results = cursor.fetchall()
    print(results)  
    print("CONECTADO!")
    return render_template("tela_atualizar_moedas.html",content=results)

@app.route('/tela_atualizar_moedas_dois', methods=['GET','POST'])
def atualizar_moedas():
    cursor = meuBanco.cursor()    
    sql = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_atualizar_moedas_dois.html", content=results)    



app.run(debug= True)