import mysql.connector as mysql

try:
    conexao = mysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='aula'
    )
    print('Conectado com sucesso!')
    cursor = conexao.cursor()
    comando = 'select * from curso'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    conexao.commit()
    conexao.close()

except Exception as err:
    print('Houve um erro ao conectar')
    print(err)