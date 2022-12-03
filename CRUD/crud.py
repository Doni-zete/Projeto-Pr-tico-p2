from conectar.conexaoBase import conectaDB
meuBanco = conectaDB()
mycursor = meuBanco.cursor()

print(meuBanco)


# ========================Criar database===============================
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

# ========================Criar Tabelas ===============================
def tabela_cliente():
  try:
    mycursor.execute(
      "CREATE TABLE `trabalhoP2_db`.`tabela_cliente` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `senha` VARCHAR(60) NOT NULL,  `email` VARCHAR(60) NOT NULL,PRIMARY KEY (`id`)) "
      )
    print('Tabela criada com sucesso!')
  except:
    print("Tabela já criada.")    


def tabela_moeda():
  try:
    mycursor.execute(
      "CREATE TABLE `trabalhoP2_db`.`tabela_moeda` ( `id` INT NOT NULL AUTO_INCREMENT , `moeda` VARCHAR(20) NOT NULL , `simbolo` VARCHAR(10) NOT NULL, `valor` VARCHAR(15) NOT NULL , `quantidade`  VARCHAR(15) NOT NULL, PRIMARY KEY (`id`)) "
      )
    print('Tabela criada com sucesso!')
  except:
    print("Tabela já criada.")   


def tabela_usuario():
  try:
    mycursor.execute(
      "CREATE TABLE `trabalhoP2_db`.`tabela_usuario` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `senha` VARCHAR(60) NOT NULL,  `email` VARCHAR(60) NOT NULL,PRIMARY KEY (`id`)) "
      )
    print('Tabela criada com sucesso!')
  except:
    print("Tabela já criada.")

def terminaConexao():
  meuBanco.commit()    

# ========================Criar tabelas de manipulação=============================


# try:
#   def cadastrarCliente(valores):

#     sql = "INSERT INTO `trabalhoP2_db`.`tbl_cliente` (`nome`, `email`, `senha`) VALUES(%s, %s, %s)"
#     vlr = (valores['nome'], valores['email'], valores['senha'])
#     print("clienteNovo: {}".format(vlr))

#     mycursor.execute(sql, vlr)
#     terminaConexao()

#     print("Dados criados com sucesso")
# except:
#   print('Dados não inseridos')



try:
  def verificaLogin(valores):
    sql = "SELECT * from `trabalhoP2_db`.`tbl_usuario` where email=%s and senha=%s"
    vlr = (valores['email'], valores['senha'])
    mycursor.execute(sql, vlr)
    print(mycursor.fetchone())
    terminaConexao()
    return 'sucesso'
except:
  print('Dados não inseridos')




  



