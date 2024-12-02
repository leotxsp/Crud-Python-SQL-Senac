# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlunoYoABzO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(561, 595)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 40, 501, 200))
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edtNome = QLineEdit(self.frame_2)
        self.edtNome.setObjectName(u"edtNome")
        self.edtNome.setStyleSheet(u"background-color: rgb(252, 255, 199);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.edtNome)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.edtEmail = QLineEdit(self.frame_6)
        self.edtEmail.setObjectName(u"edtEmail")
        self.edtEmail.setStyleSheet(u"background-color: rgb(252, 255, 199);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.edtEmail)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.CbCurso = QComboBox(self.frame_3)
        self.CbCurso.setObjectName(u"CbCurso")

        self.horizontalLayout_2.addWidget(self.CbCurso)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnInserir = QPushButton(self.frame_5)
        self.btnInserir.setObjectName(u"btnInserir")
        self.btnInserir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnInserir.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(243, 134, 2);")

        self.verticalLayout_2.addWidget(self.btnInserir)

        self.btnAlterar = QPushButton(self.frame_5)
        self.btnAlterar.setObjectName(u"btnAlterar")
        self.btnAlterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAlterar.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(243, 134, 2);")

        self.verticalLayout_2.addWidget(self.btnAlterar)

        self.btnExcluir = QPushButton(self.frame_5)
        self.btnExcluir.setObjectName(u"btnExcluir")
        self.btnExcluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExcluir.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(243, 134, 2);")

        self.verticalLayout_2.addWidget(self.btnExcluir)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(11)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 270, 471, 251))
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Aluno", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">Curso</span></p></body></html>", None))
        self.btnInserir.setText(QCoreApplication.translate("Form", u"Inserir", None))
        self.btnAlterar.setText(QCoreApplication.translate("Form", u"alterar", None))
        self.btnExcluir.setText(QCoreApplication.translate("Form", u"Excluir", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"E-mail", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Curso", None));
    # retranslateUi

