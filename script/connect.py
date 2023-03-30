import mysql.connector
#importa a biblioteca mysql-connector
from mysql.connector import errorcode
#importando um código de erro da biblioteca mysql


try:

  #criandoo uma variável para fazer a conexão entre o Python e o MySQL
  mydb = mysql.connector.connect(
    host="your host", 
    user="your user",
    password="your password"
    database="your database",
  )

#chamando o Error code, se caso a conexão acima não foi bem sucedida
except mysql.connector.Error as e:
  if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Algo deu errado com o user ou password!")
  
  elif e.errno == errorcode.ER_BAD_DB_ERROR:
    print("Banco de dados não existe.")

  else:
    print(e)

#Se a conexão foi bem sucedida
if mydb.is_connected():
  print("Conexão bem sucedida!")
