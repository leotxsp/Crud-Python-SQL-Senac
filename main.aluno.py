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
        self.montarTabela()
        self.tableWidget.doubleClicked.connect(self.selecionar)
        self.btnExcluir.clicked.connect(self.excluir)
        self.btnAlterar.clicked.connect(self.alterar)
        self.montarTabela()
        self.montarCombo()
        
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
                self.tableWidget.setItem(linha,3,QtWidgets.QTableWidgetItem(str(aluno.curso)))

app = QtWidgets.QApplication(sys.argv)
window = Main()
window.show()
app.exec()
