#conexão com banco de dados

#instalar o drive conector
#mysql connector
#o drive é um tradutor python --> mysql
import mysql.connector

def conectar():
    #conexão com o banco de dados
    #o drive tenta abrir uma conexão
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="projetoindustrial",
        port=3306
)
    return conexao