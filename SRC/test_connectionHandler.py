from connectionHandler import ConnectionHandler,cursor

with ConnectionHandler() as test:
    comando = 'select * from curso'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)