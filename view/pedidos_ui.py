# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogPedidos.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_janela_pedidos(object):
    def setupUi(self, janela_pedidos):
        if not janela_pedidos.objectName():
            janela_pedidos.setObjectName(u"janela_pedidos")
        janela_pedidos.resize(564, 302)
        self.verticalLayout = QVBoxLayout(janela_pedidos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_pedidos_nome_pedidos = QLabel(janela_pedidos)
        self.lbl_pedidos_nome_pedidos.setObjectName(u"lbl_pedidos_nome_pedidos")
        self.lbl_pedidos_nome_pedidos.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.lbl_pedidos_nome_pedidos)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_pedidos_maior = QWidget(janela_pedidos)
        self.widget_pedidos_maior.setObjectName(u"widget_pedidos_maior")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_pedidos_maior)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_pedidos_nome_criar_pedidos = QLabel(self.widget_pedidos_maior)
        self.lbl_pedidos_nome_criar_pedidos.setObjectName(u"lbl_pedidos_nome_criar_pedidos")

        self.verticalLayout_2.addWidget(self.lbl_pedidos_nome_criar_pedidos)

        self.lbl_pedidos_nome_produto = QLabel(self.widget_pedidos_maior)
        self.lbl_pedidos_nome_produto.setObjectName(u"lbl_pedidos_nome_produto")

        self.verticalLayout_2.addWidget(self.lbl_pedidos_nome_produto)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_pedidos_produto = QLineEdit(self.widget_pedidos_maior)
        self.txt_pedidos_produto.setObjectName(u"txt_pedidos_produto")

        self.horizontalLayout_2.addWidget(self.txt_pedidos_produto)

        self.btn_pedidos_buscar_produto = QPushButton(self.widget_pedidos_maior)
        self.btn_pedidos_buscar_produto.setObjectName(u"btn_pedidos_buscar_produto")

        self.horizontalLayout_2.addWidget(self.btn_pedidos_buscar_produto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.comboBox_pedidos_produto = QComboBox(self.widget_pedidos_maior)
        self.comboBox_pedidos_produto.setObjectName(u"comboBox_pedidos_produto")

        self.verticalLayout_2.addWidget(self.comboBox_pedidos_produto)

        self.lbl_pedidos_nome_quantidade = QLabel(self.widget_pedidos_maior)
        self.lbl_pedidos_nome_quantidade.setObjectName(u"lbl_pedidos_nome_quantidade")

        self.verticalLayout_2.addWidget(self.lbl_pedidos_nome_quantidade)

        self.txt_pedidos_quantidade = QLineEdit(self.widget_pedidos_maior)
        self.txt_pedidos_quantidade.setObjectName(u"txt_pedidos_quantidade")

        self.verticalLayout_2.addWidget(self.txt_pedidos_quantidade)

        self.btn_pedidos_adicionar = QPushButton(self.widget_pedidos_maior)
        self.btn_pedidos_adicionar.setObjectName(u"btn_pedidos_adicionar")

        self.verticalLayout_2.addWidget(self.btn_pedidos_adicionar)

        self.btn_pedidos_finalizar_pedidos = QPushButton(self.widget_pedidos_maior)
        self.btn_pedidos_finalizar_pedidos.setObjectName(u"btn_pedidos_finalizar_pedidos")

        self.verticalLayout_2.addWidget(self.btn_pedidos_finalizar_pedidos)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.widget_pedidos_menor = QWidget(self.widget_pedidos_maior)
        self.widget_pedidos_menor.setObjectName(u"widget_pedidos_menor")
        self.verticalLayout_4 = QVBoxLayout(self.widget_pedidos_menor)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_pedidos_nome_receber_pedidos = QLabel(self.widget_pedidos_menor)
        self.lbl_pedidos_nome_receber_pedidos.setObjectName(u"lbl_pedidos_nome_receber_pedidos")

        self.verticalLayout_3.addWidget(self.lbl_pedidos_nome_receber_pedidos)

        self.tb_lista_produtos = QTableWidget(self.widget_pedidos_menor)
        if (self.tb_lista_produtos.columnCount() < 2):
            self.tb_lista_produtos.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_lista_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_lista_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_lista_produtos.setObjectName(u"tb_lista_produtos")
        self.tb_lista_produtos.verticalHeader().hide()
        self.tb_lista_produtos.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_lista_produtos.setEditTriggers(QTableWidget.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.tb_lista_produtos)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_pedidos_remover = QPushButton(self.widget_pedidos_menor)
        self.btn_pedidos_remover.setObjectName(u"btn_pedidos_remover")

        self.horizontalLayout_4.addWidget(self.btn_pedidos_remover)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addWidget(self.widget_pedidos_menor)


        self.horizontalLayout.addWidget(self.widget_pedidos_maior)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(janela_pedidos)

        QMetaObject.connectSlotsByName(janela_pedidos)
    # setupUi

    def retranslateUi(self, janela_pedidos):
        janela_pedidos.setWindowTitle(QCoreApplication.translate("janela_pedidos", u"Dialog", None))
        self.lbl_pedidos_nome_pedidos.setText(QCoreApplication.translate("janela_pedidos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Pedidos</span></p></body></html>", None))
        self.lbl_pedidos_nome_criar_pedidos.setText(QCoreApplication.translate("janela_pedidos", u"Criar pedidos", None))
        self.lbl_pedidos_nome_produto.setText(QCoreApplication.translate("janela_pedidos", u"Produto", None))
        self.btn_pedidos_buscar_produto.setText(QCoreApplication.translate("janela_pedidos", u"Buscar", None))
        self.lbl_pedidos_nome_quantidade.setText(QCoreApplication.translate("janela_pedidos", u"Quantidade", None))
        self.btn_pedidos_adicionar.setText(QCoreApplication.translate("janela_pedidos", u"Adicionar produto", None))
        self.btn_pedidos_finalizar_pedidos.setText(QCoreApplication.translate("janela_pedidos", u"Finalizar pedido", None))
        self.lbl_pedidos_nome_receber_pedidos.setText(QCoreApplication.translate("janela_pedidos", u"Lista de produtos", None))
        ___qtablewidgetitem = self.tb_lista_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("janela_pedidos", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_lista_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("janela_pedidos", u"Quantidade", None));
        self.btn_pedidos_remover.setText(QCoreApplication.translate("janela_pedidos", u"Remover", None))
    # retranslateUi

