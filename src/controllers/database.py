import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='zeus'
    )
    return conexao
