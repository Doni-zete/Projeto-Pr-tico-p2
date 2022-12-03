from flask import Flask, request, render_template, redirect
from CRUD.crud import criarBases, verificaLogin, meuBanco
# import pandas as pd
import json

app = Flask(__name__)
criarBases()

# app.secret_key ="123hudsadasdw"

@app.route("/")
def Inicio():
    return render_template('tela_incial.html')


@app.route('/tela_cadatro_usuario', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        informacao = request.form
        nome = informacao['nome']
        senha = informacao['senha']
        email = informacao['email']

        cur = meuBanco.cursor()
        cur.execute(
            "INSERT INTO trabalhoP2_db.tabela_usuario(nome,email,senha) VALUES (%s, %s,%s)", (nome, email, senha))
        meuBanco.commit()
        cur.close()
        # redireciona para a pagina inicial
        return redirect('/')
    return render_template('tela_cadatro_usuario.html')


@app.route("/tela_login")
def Login():
    return render_template('tela_login.html')


@app.route("/tela_menu")
def menu_aplicacao():
    return render_template('tela_menu.html')


@app.route('/tela_listar_clientes')
def listar_cliente():
    cursor = meuBanco.cursor()
    sql = "SELECT *  FROM trabalhoP2_db.tabela_cliente"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_listar_clientes.html", content=results)

@app.route('/tela_listar_usuarios')
def listar_usuairos():
    cursor = meuBanco.cursor()
    sql = "SELECT *  FROM trabalhoP2_db.tabela_usuario"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_listar_clientes.html", content=results)


@app.route('/tela_atualizar_clientes_dois')
def atualizar_clientes_dois():
    cursor = meuBanco.cursor()
    sql = "SELECT *  FROM trabalhoP2_db.tabela_cliente"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_atualizar_clientes_dois.html", content=results)


@app.route("/deletar_cliente")
def deletar():
    cursor = meuBanco.cursor()
    sql = "DELETE FROM trabalhoP2_db.tabela_cliente WHERE id = %s"
    cursor.execute(sql, (request.args.get('id'),))
    meuBanco.commit()
    return redirect('/tela_listar_clientes')


@app.route("/tela_inserir_cliente", methods=['GET', 'POST'])
def inserir_cliente():
    if request.method == "POST":
        informacao = request.form
        nome = informacao['nome']
        senha = informacao['senha']
        email = informacao['email']

        cur = meuBanco.cursor()
        cur.execute(
            "INSERT INTO trabalhoP2_db.tabela_cliente(nome,email,senha) VALUES (%s, %s,%s)", (nome, email, senha))
        meuBanco.commit()
        cur.close()
        # return redirect('/tela_inserir_cliente')
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
        cursor.execute(sql, (nome, senha, email,  id))
        meuBanco.commit()

        cursor = meuBanco.cursor()
        sql = "SELECT * FROM trabalhoP2_db.tabela_cliente WHERE id = %s "
        cursor.execute(sql, (request.args.get('id'),))

        # cursor.execute(sql)
        # meuBanco.commit()
        results = cursor.fetchall()
        print(results)
        print("CONECTADO!")
        return render_template("tela_atualizar_clientes.html", content=results)

    else:
        cursor = meuBanco.cursor()
        sql = "SELECT * FROM trabalhoP2_db.tabela_cliente WHERE id = %s"
        # cursor.execute(sql)
        cursor.execute(sql, (request.args.get('id'),))

        results = cursor.fetchall()
        print(results)
        print("CONECTADO!")
        return render_template("tela_atualizar_clientes.html", content=results)


@app.route('/tela_listar_moedas')
def listar_moedas():
    cursor = meuBanco.cursor()
    sql = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_listar_moedas.html", content=results)


@app.route("/tela_inserir_moeda", methods=["GET", "POST"])
def inserir_moeda():
    if request.method == "POST":
        informacao = request.form
        moeda = informacao['moeda']
        simbolo = informacao['simbolo']
        valor = informacao['valor']
        quantidade = informacao['quantidade']

        cur = meuBanco.cursor()
        cur.execute("INSERT INTO trabalhoP2_db.tabela_moeda(moeda,simbolo,valor,quantidade) VALUES (%s, %s,%s,%s)",
                    (moeda, simbolo, valor, quantidade))
        meuBanco.commit()
        cur.close()
    return render_template('tela_inserir_moeda.html')


@app.route("/deletar_moeda")
def deletar_moeda():
    cursor = meuBanco.cursor()
    sql = "DELETE FROM trabalhoP2_db.tabela_moeda WHERE id = %s"
    cursor.execute(sql, (request.args.get('id'),))
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
        cursor.execute(sql, (moeda, simbolo, valor, quantidade,  id))
        meuBanco.commit()

        cursor = meuBanco.cursor()
        sql = "SELECT * FROM trabalhoP2_db.tabela_moeda WHERE id = %s "
        cursor.execute(sql, (request.args.get('id'),))

        # cursor.execute(sql)
        # meuBanco.commit()
        results = cursor.fetchall()
        print(results)
        print("CONECTADO!")
        return render_template("tela_atualizar_moedas.html", content=results)

    else:
        cursor = meuBanco.cursor()
        sql = "SELECT * FROM trabalhoP2_db.tabela_moeda WHERE id = %s"
        # cursor.execute(sql)
        cursor.execute(sql, (request.args.get('id'),))

        results = cursor.fetchall()
        print(results)
        print("CONECTADO!")
        return render_template("tela_atualizar_moedas.html", content=results)


@app.route('/tela_atualizar_moedas_dois')
def atualizar_moedas():
    cursor = meuBanco.cursor()
    sql = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return render_template("tela_atualizar_moedas_dois.html", content=results)


@app.route('/tela_sobre')
def sobre():
    return render_template("tela_sobre.html")


@app.route('/tela_extrair_dados')
def extrair_dados():
    cursor = meuBanco.cursor()
    sql = " SELECT * FROM trabalhoP2_db.tabela_cliente"
    # sqlm = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    # cursor.execute(sqlm)
    clientes = cursor.fetchall()


    cursor = meuBanco.cursor()
    sql = " SELECT * FROM trabalhoP2_db.tabela_moeda"
    # sqlm = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    # cursor.execute(sqlm)
    moedas = cursor.fetchall()
    # print(moedas)


    cursor = meuBanco.cursor()
    sql = " SELECT * FROM trabalhoP2_db.tabela_usuario"
    # sqlm = "SELECT *  FROM trabalhoP2_db.tabela_moeda"
    cursor.execute(sql)
    # cursor.execute(sqlm)
    usuarios = cursor.fetchall()

    return render_template("tela_extrair_dados.html", content=(clientes, moedas,usuarios))


def extrair_salvar(tabela_nome, nome_arquivo):
    print("iniciando scrapping...")

    #abrindo conexao com a base de dados
    cursor = meuBanco.cursor()
    
    #preparando a query adicinando nome da tabela na string
    sql = " SELECT * FROM trabalhoP2_db.{}".format(tabela_nome)


    #executando query na base d e dados
    cursor.execute(sql)
    # ira armazenar nome das colunas das tabelas
    headers = []

    #pega o nome das colunas das tabelas e salvar dentro da variaval 'headers'
    for item in cursor.description:
      headers.append(item[0])

    # Recebe valores da base de dados
    dados = cursor.fetchall()

    # formata os dados para adicionar em uma lista de objetos com nome da coluna e o valor
    dados_object = []
    for item in dados:
      obcj = {}
      for index, ite in enumerate(item):
        obcj[headers[index]] = ite
      dados_object.append(obcj)

    #Converte os dados para json
    objeto_json = json.dumps(dados_object)

    #Salvando o arquivo no diretorio static para que o servidor possa  deixar visiel  parao  download
    with open("static/temp/{}.json".format(nome_arquivo), "w") as arquivo_saida:
        arquivo_saida.write(objeto_json)
    # print(objeto_json)

    print("Finalizado!")

#  quando clica no botão salvar e chamada no front 
@app.route('/button_extrair', methods=["GET", "POST"])
def raspando_dados():
    # função chamada para salvar dados do cliente
    extrair_salvar("tabela_cliente", "clientes")
    # função chamada para salvar dados da moeda
    extrair_salvar("tabela_moeda", "moedas")

    extrair_salvar("tabela_usuario", "usuarios")

    return redirect('/tela_extrair_dados')
    # return render_template("button_extrair.html")


app.run(debug=True)
