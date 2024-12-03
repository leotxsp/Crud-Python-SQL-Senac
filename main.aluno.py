import sys
from PySide6 import QtWidgets
from tela.ui_Aluno import Ui_Form
from SRC.Entities.Aluno import Aluno
from SRC.Entities.Curso import Curso

class Main(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.btnInserir.clicked.connect(self.buscar())
        self.lista = []
        self.listaCurso = []
        self.cursoSelecionado = Curso()
        self.alunoSelecionado = Aluno()
        
        
        self.btnInserir.clicked.connect(self.incluir)
        self.tableWidget.doubleClicked.connect(self.selecionar)
        self.btnExcluir.clicked.connect(self.excluir)
        self.btnAlterar.clicked.connect(self.alterar)
        self.montarTabela()
        self.buscarCurso()
        
    def buscarCurso(self):
            try:
                curso = Curso()
                self.listaCurso = curso.buscar()
                for i in self.listaCurso:
                    print(i.nome)
                    self.CbCurso.addItem(i.nome)
                print("busca realizada com sucesoo")
                self.limpar()
            except Exception as erro:
                print("Erro ao Buscar")
                print(erro)  
            
        
    def montarTabela(self):
        self.buscar()
        linha = 0
        self.tableWidget.setRowCount(len(self.lista))
        for aluno in self.lista:
            self.tableWidget.setStyleSheet("QTableWidget::item {border: 0px; padding: 5px; background-color: rgb(15, 9, 6);}")
            print(aluno)
            self.tableWidget.setItem(linha,0,QtWidgets.QTableWidgetItem(str(aluno.idAluno)))
            self.tableWidget.setItem(linha,1,QtWidgets.QTableWidgetItem(str(aluno.nome)))
            self.tableWidget.setItem(linha,2,QtWidgets.QTableWidgetItem(str(aluno.email)))
            self.tableWidget.setItem(linha,3,QtWidgets.QTableWidgetItem(str(aluno.curso.nome)))
            linha+=1
        
        
    def selecionar(self):
        item = self.tableWidget.currentRow()
        self.alunoSelecionado = self.lista[item]
        self.edtNome.setText(str(self.alunoSelecionado.nome))
        self.edtEmail.setText(str(self.alunoSelecionado.email))
        
    def excluir(self):
        try:
            self.alunoSelecionado.excluir()
            self.montarTabela()
            self.limpar()
        except Exception as erro:
            print("Erro ao excluir")
            print(erro)
    
    
        
    def buscar(self):
            try:
                aluno = Aluno()
                self.lista = aluno.buscar()
                print("busca realizada com sucesoo")
                self.limpar()
            except Exception as erro:
                print("Erro ao Buscar")
                print(erro)
            
    def alterar(self):
        try:
            self.alunoSelecionado.nome = self.edtNome.text()
            self.alunoSelecionado.email = self.edtEmail.text()
            indexCombo = self.CbCurso.currentIndex()
            curso = self.listaCurso[indexCombo]
            self.alunoSelecionado.curso = curso
            self.alunoSelecionado.alterar()
            self.montarTabela()
            self.limpar()
        except Exception as erro:
            print("Erro ao excluir")
            print(erro)
        
            
    def incluir(self):
        try:
            nome = self.edtNome.text()
            email = self.edtEmail.text()
            indexCombo = self.CbCurso.currentIndex()
            curso = self.listaCurso[indexCombo]
            aluno = Aluno(0,nome,email,curso)
            aluno.incluir()
            self.montarTabela()
            self.limpar()
            print(curso.buscar())
            print("incluido com sucesso")
            self.limpar()
        except Exception as erro:
            print("Erro ao Inserir")
            print(erro)
            
    def limpar(self):
        self.edtNome.clear()
        self.edtEmail.clear()
            
app = QtWidgets.QApplication(sys.argv)
window = Main()
window.show()
app.exec()
