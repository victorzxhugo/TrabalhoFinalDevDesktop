# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogCadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_janela_cadastro(object):
    def setupUi(self, janela_cadastro):
        if not janela_cadastro.objectName():
            janela_cadastro.setObjectName(u"janela_cadastro")
        janela_cadastro.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(janela_cadastro)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_cadastro_nome_cadastro = QLabel(janela_cadastro)
        self.lbl_cadastro_nome_cadastro.setObjectName(u"lbl_cadastro_nome_cadastro")

        self.verticalLayout.addWidget(self.lbl_cadastro_nome_cadastro)

        self.lbl_cadastro_nome_nome = QLabel(janela_cadastro)
        self.lbl_cadastro_nome_nome.setObjectName(u"lbl_cadastro_nome_nome")

        self.verticalLayout.addWidget(self.lbl_cadastro_nome_nome)

        self.txt_cadastro_nome = QLineEdit(janela_cadastro)
        self.txt_cadastro_nome.setObjectName(u"txt_cadastro_nome")

        self.verticalLayout.addWidget(self.txt_cadastro_nome)

        self.lbl_cadastro_preco = QLabel(janela_cadastro)
        self.lbl_cadastro_preco.setObjectName(u"lbl_cadastro_preco")

        self.verticalLayout.addWidget(self.lbl_cadastro_preco)

        self.txt_cadastro_preco = QLineEdit(janela_cadastro)
        self.txt_cadastro_preco.setObjectName(u"txt_cadastro_preco")

        self.verticalLayout.addWidget(self.txt_cadastro_preco)

        self.lbl_cadastro_categoria = QLabel(janela_cadastro)
        self.lbl_cadastro_categoria.setObjectName(u"lbl_cadastro_categoria")

        self.verticalLayout.addWidget(self.lbl_cadastro_categoria)

        self.comboBox_cadastro_categoria = QComboBox(janela_cadastro)
        self.comboBox_cadastro_categoria.setObjectName(u"comboBox_cadastro_categoria")
        self.comboBox_cadastro_categoria.addItem('Selecione um item')
        self.comboBox_cadastro_categoria.addItem('Alimentos')
        self.comboBox_cadastro_categoria.addItem('Bebidas')
        self.comboBox_cadastro_categoria.addItem('Padaria')
        self.comboBox_cadastro_categoria.addItem('Limpeza')
        self.comboBox_cadastro_categoria.addItem('Higiene Pessoal')



        self.verticalLayout.addWidget(self.comboBox_cadastro_categoria)

        self.btn_cadastro_cadastrar = QPushButton(janela_cadastro)
        self.btn_cadastro_cadastrar.setObjectName(u"btn_cadastro_cadastrar")

        self.verticalLayout.addWidget(self.btn_cadastro_cadastrar)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(janela_cadastro)

        QMetaObject.connectSlotsByName(janela_cadastro)
    # setupUi

    def retranslateUi(self, janela_cadastro):
        janela_cadastro.setWindowTitle(QCoreApplication.translate("janela_cadastro", u"Dialog", None))
        self.lbl_cadastro_nome_cadastro.setText(QCoreApplication.translate("janela_cadastro", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Cadastro de Produtos</span></p></body></html>", None))
        self.lbl_cadastro_nome_nome.setText(QCoreApplication.translate("janela_cadastro", u"Nome", None))
        self.txt_cadastro_nome.setText("")
        self.lbl_cadastro_preco.setText(QCoreApplication.translate("janela_cadastro", u"Pre\u00e7o", None))
        self.txt_cadastro_preco.setText("")
        self.lbl_cadastro_categoria.setText(QCoreApplication.translate("janela_cadastro", u"Categoria", None))
        self.btn_cadastro_cadastrar.setText(QCoreApplication.translate("janela_cadastro", u"Cadastrar", None))
    # retranslateUi

