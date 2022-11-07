import mysql.connector

# 
def conectaDB():
  try:
    meuBanco = mysql.connector.connect(
      host="localhost",
      user="root",
      port ="3307",
      password="12345678",
      )
   
    print("Conexão realizada com sucesso!!!")
  except Exception as erro:
    print(erro)

  return meuBanco


