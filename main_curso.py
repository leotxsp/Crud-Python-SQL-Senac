import sys
from PySide6 import QtWidgets
from tela.ui_Curso import Ui_Form
from SRC.Entities.Curso import Curso

class Main(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.lista = []
        self.cursoSelecionado = Curso()
        self.btnInserir.clicked.connect(self.incluir)
        self.montarTabela()
        self.tableWidget.doubleClicked.connect(self.selecionar)
    
    def incluir(self):
        try:
            nome = self.edtNome.text()
            ch = int(self.ednCH.text())
            curso = Curso(0,nome,ch)
            curso.incluir()
            print(curso.buscar())
            print("incluido com sucesso")
        except Exception as erro:
            print("Erro ao Inserir")
            print(erro)
        
    def buscar(self):
        try:
            curso = Curso()
            self.lista = curso.buscar()
            print("busca realizada com sucesoo")
        except Exception as erro:
            print("Erro ao Buscar")
            print(erro)
            
    def montarTabela(self):
        self.buscar()
        linha = 0
        self.tableWidget.setRowCount(len(self.lista))
        for curso in self.lista:
            self.tableWidget.setStyleSheet("QTableWidget::item {border: 0px; padding: 5px; background-color: rgb(15, 9, 6);}")
            print(curso)
            self.tableWidget.setItem(linha,0,QtWidgets.QTableWidgetItem(str(curso.idcurso)))
            self.tableWidget.setItem(linha,1,QtWidgets.QTableWidgetItem(str(curso.nome)))
            self.tableWidget.setItem(linha,2,QtWidgets.QTableWidgetItem(str(curso.ch)))
            linha+=1
    def selecionar(self):
        item = self.tableWidget.currentRow()
        self.cursoSelecionado = self.lista[item]
        self.edtNome.setText(str(self.cursoSelecionado.nome))
        self.ednCH.setText(str(self.cursoSelecionado.ch))
app = QtWidgets.QApplication(sys.argv)

window = Main()
window.show()
app.exec()