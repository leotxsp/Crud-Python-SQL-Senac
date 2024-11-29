import mysql.connector as mysql

def conequisao():
    try:
        conexao = mysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='aula'
        )
        print('Conectado com sucesso!')
        return conexao
    except Exception as err:
        print('Houve um erro ao conectar', err)
        
def incluir():
    conexao = conequisao()
    cursor = conexao.cursor()
    nome = input("informe o curso: ")
    ch = input("Informe a carga horaria: ")
    sql = f'insert into curso (nome,ch), values ("{nome}",{ch})'
    cursor.execute(sql)
    conexao.commit()
    
def exibir():
    conexao = conequisao()
    cursor = conexao.cursor()
    sql = 'Select * from curso'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for curso in resultado:
        print("\nid:",curso[0])
        print("Nome:",curso[1])
        print("CH: ",curso[2])
        print("\n",30*"=")
        
def menu():
    print("\n",15*"=","MENU",15*"=")
    print("1 - INCLUIR")
    print("2 - EXIBIR")
    print("9 - ENCERRAR")
    print(30*"=")

while True:
    menu()
    opcao = input("Informe uma opção: ")
    if(opcao == "1"):
        incluir()
    elif(opcao == "2"):
        exibir()
    elif(opcao == "9"):
        break
    else:
        print("Opção invalida")