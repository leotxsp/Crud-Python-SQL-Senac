from DB.Conexao import conectar
from SRC.Entities.Curso import Curso
class Aluno:
    def __init__(self, idAluno = None ,email = None,nome = None, curso = None):
        self.idAluno = idAluno
        self.email = email
        self.nome = nome
        self.curso = curso
        
    def incluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'insert into aluno (nome,email,Curso_idCurso) values ("{self.nome}","{self.email}",{self.curso.idcurso})'
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def excluir(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'delete from aluno where idAluno = {self.idAluno}'
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def alterar(self):
        con = conectar()
        cursor = con.cursor()
        sql = f'update aluno set nome = "{self.nome}", email= {self.email},Curso_idCurso = {self.curso.idcurso}  where idAluno={self.idAluno}'
        cursor.execute(sql)
        con.commit()
        con.close()
    
    def buscar(self):
        con = conectar()
        cursor = con.cursor()
        sql = 'select * from aluno'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        lista = []
        for item in resultado:
            curso = Curso()
            cursoSelecionado = curso.buscarUM(item[3])
            aluno = Aluno(item[0],item[1],item[2],cursoSelecionado)
            lista.append(aluno)
        con.close()
        return lista
