from DB.Conexao import conectar
class Curso:
    def __init__(self, idcurso = None ,nome = None,ch = None):
        self.idcurso = idcurso
        self.nome = nome
        self.ch = ch
        
    def incluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'insert into curso (nome,ch) values ("{self.nome}",{self.ch})'
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def excluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'delete from curso where idcurso = {self.idcurso}'
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def alterar(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'update curso set nome = "{self.nome}", ch= {self.ch} where idCurso={self.idcurso}'
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def buscar(self):
        con = conectar()
        cursor = con.cursor()
        sql = 'select * from curso'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            curso = Curso(item[0],item[1],item[2])
            lista.append(curso)
        con.close()
        return lista

    def buscarUM(self,idcurso):
        con = conectar()
        cursor = con.cursor()
        sql = f'select from curso where idcurso = {idcurso}'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        item = resultado[0]
        curso = Curso(item[0],item[1],item[2])
        con.close()
        return curso
