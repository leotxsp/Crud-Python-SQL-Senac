import mysql.connector as mysql
def conectar():
    conexao = mysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='aula'
    )
    return conexao