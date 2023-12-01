# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogVendas.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_janela_vendas(object):
    def setupUi(self, janela_vendas):
        if not janela_vendas.objectName():
            janela_vendas.setObjectName(u"janela_vendas")
        janela_vendas.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(janela_vendas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_venda_nome_vendas = QLabel(janela_vendas)
        self.lbl_venda_nome_vendas.setObjectName(u"lbl_venda_nome_vendas")

        self.verticalLayout.addWidget(self.lbl_venda_nome_vendas)

        self.lbl_venda_nome_produto = QLabel(janela_vendas)
        self.lbl_venda_nome_produto.setObjectName(u"lbl_venda_nome_produto")

        self.verticalLayout.addWidget(self.lbl_venda_nome_produto)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_venda_produto = QLineEdit(janela_vendas)
        self.txt_venda_produto.setObjectName(u"txt_venda_produto")

        self.horizontalLayout.addWidget(self.txt_venda_produto)

        self.btn_venda_buscar_produto = QPushButton(janela_vendas)
        self.btn_venda_buscar_produto.setObjectName(u"btn_venda_buscar_produto")

        self.horizontalLayout.addWidget(self.btn_venda_buscar_produto)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.comboBox_venda_produto = QComboBox(janela_vendas)
        self.comboBox_venda_produto.setObjectName(u"comboBox_venda_produto")

        self.verticalLayout.addWidget(self.comboBox_venda_produto)

        self.lbl_venda_nome_quantidade = QLabel(janela_vendas)
        self.lbl_venda_nome_quantidade.setObjectName(u"lbl_venda_nome_quantidade")

        self.verticalLayout.addWidget(self.lbl_venda_nome_quantidade)

        self.txt_venda_qtd = QLineEdit(janela_vendas)
        self.txt_venda_qtd.setObjectName(u"txt_venda_qtd")

        self.verticalLayout.addWidget(self.txt_venda_qtd)

        self.btn_venda_adicionar = QPushButton(janela_vendas)
        self.btn_venda_adicionar.setObjectName(u"btn_venda_adicionar")

        self.verticalLayout.addWidget(self.btn_venda_adicionar)

        self.btn_venda_finalizar = QPushButton(janela_vendas)
        self.btn_venda_finalizar.setObjectName(u"btn_venda_finalizar")

        self.verticalLayout.addWidget(self.btn_venda_finalizar)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(janela_vendas)

        QMetaObject.connectSlotsByName(janela_vendas)
    # setupUi

    def retranslateUi(self, janela_vendas):
        janela_vendas.setWindowTitle(QCoreApplication.translate("janela_vendas", u"Dialog", None))
        self.lbl_venda_nome_vendas.setText(QCoreApplication.translate("janela_vendas", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Vendas</span></p></body></html>", None))
        self.lbl_venda_nome_produto.setText(QCoreApplication.translate("janela_vendas", u"Produto", None))
        self.btn_venda_buscar_produto.setText(QCoreApplication.translate("janela_vendas", u"Buscar", None))
        self.lbl_venda_nome_quantidade.setText(QCoreApplication.translate("janela_vendas", u"Quantidade", None))
        self.btn_venda_adicionar.setText(QCoreApplication.translate("janela_vendas", u"Adicionar", None))
        self.btn_venda_finalizar.setText(QCoreApplication.translate("janela_vendas", u"Finalizar venda", None))
    # retranslateUi

