from conectar.conexaoBase import conectaDB

meuBanco = conectaDB()
mycursor = meuBanco.cursor()

print(meuBanco)


def criarBases():
  try:
      mycursor.execute("create DATABASE trabalhoP2_db")
      tabela_usuario()
      tabela_cliente()
      tabela_moeda()
      print("Database Criada Com sucesso!")
      # terminaConexao()
  except:
    print("Database já existe!")


def tabela_cliente():
  try:
    mycursor.execute(
      "CREATE TABLE `trabalhoP2_db`.`tabela_cliente` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `sobrenome` VARCHAR(60) NOT NULL , `endereco` VARCHAR(100) NOT NULL , `telefone` VARCHAR(15) NOT NULL , `cpf` VARCHAR(11) NOT NULL, `email` VARCHAR(60) NOT NULL, `senha` VARCHAR(60) NOT NULL, PRIMARY KEY (`id`)) "
      )
    print('Tabela criada com sucesso!')
  except:
    print("Tabela já criada.")    


def tabela_moeda():
  try:
    mycursor.execute(
      "CREATE TABLE `trabalhoP2_db`.`tabela_moeda` ( `id` INT NOT NULL AUTO_INCREMENT , `moeda` VARCHAR(20) NOT NULL , `simbolo` VARCHAR(10) NOT NULL, `valor` VARCHAR(15) NOT NULL , PRIMARY KEY (`id`)) "
      )
    print('Tabela criada com sucesso!')
  except:
    print("Tabela já criada.")   


def tabela_usuario():
  try:
    mycursor.execute(
      "CREATE TABLE `trabalhoP2_db`.`tbl_usuario` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `email` VARCHAR(60) NOT NULL , `senha` VARCHAR(60) NOT NULL , PRIMARY KEY (`id`))"
      )
    print('Tabela criada com sucesso!')
  except:
    print("Tabela já criada.")

def terminaConexao():
  meuBanco.commit()    

# Tabelas criadas


try:
  def cadastrarCliente(valores):

    sql = "INSERT INTO `trabalhoP2_db`.`tbl_cliente` (`nome`, `sobrenome`, `endereco`, `telefone`, `cpf`, `email`, `senha`) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    vlr = (valores['nome'], valores['sobrenome'], valores['endereco'], valores['telefone'], valores['cpf'], valores['email'], valores['senha'])
    print("clienteNovo: {}".format(vlr))

    mycursor.execute(sql, vlr)
    terminaConexao()

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')



try:
  def verificaLogin(valores):
    sql = "SELECT * from `trabalhoP2_db`.`tbl_usuario` where email=%s and senha=%s"
    vlr = (valores['email'], valores['senha'])
    mycursor.execute(sql, vlr)
    # print("Valores da base {}".format(mycursor.fetchone()))
    # resu = mycursor.fetchone()
    print(mycursor.fetchone())
    terminaConexao()
    return 'sucesso'
except:
  print('Dados não inseridos')