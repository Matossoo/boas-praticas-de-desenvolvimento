import mysql.connector

def conectar():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="metalsul_industrial",
        port=3306

)
    
    return conexao