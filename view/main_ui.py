# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTFinal.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from view import resource

class Ui_janela_QTFinal(object):
    def setupUi(self, janela_QTFinal):
        if not janela_QTFinal.objectName():
            janela_QTFinal.setObjectName(u"janela_QTFinal")
        janela_QTFinal.resize(714, 533)
        self.centralwidget = QWidget(janela_QTFinal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setInputMethodHints(Qt.ImhNone)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_qtfinal_logo_principal = QWidget(self.centralwidget)
        self.widget_qtfinal_logo_principal.setObjectName(u"widget_qtfinal_logo_principal")
        self.widget_qtfinal_logo_principal.setMaximumSize(QSize(16777215, 120))
        self.widget_qtfinal_logo_principal.setStyleSheet(u"image:url(:/icon/warehouse_1585206.png)")
        self.verticalLayout = QVBoxLayout(self.widget_qtfinal_logo_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(678, 99, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widget_qtfinal_logo_principal)

        self.widget_qtfinal_todas_opcoes = QWidget(self.centralwidget)
        self.widget_qtfinal_todas_opcoes.setObjectName(u"widget_qtfinal_todas_opcoes")
        self.verticalLayout_4 = QVBoxLayout(self.widget_qtfinal_todas_opcoes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_qtfinal_nome_gerenciamento_de_estoque = QLabel(self.widget_qtfinal_todas_opcoes)
        self.lbl_qtfinal_nome_gerenciamento_de_estoque.setObjectName(u"lbl_qtfinal_nome_gerenciamento_de_estoque")

        self.verticalLayout_3.addWidget(self.lbl_qtfinal_nome_gerenciamento_de_estoque)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_qtfinal_imagem_cadastro_de_produtos = QLabel(self.widget_qtfinal_todas_opcoes)
        self.lbl_qtfinal_imagem_cadastro_de_produtos.setObjectName(u"lbl_qtfinal_imagem_cadastro_de_produtos")
        self.lbl_qtfinal_imagem_cadastro_de_produtos.setStyleSheet(u"image: url(:/icon/distribution_4237529.png)")

        self.horizontalLayout.addWidget(self.lbl_qtfinal_imagem_cadastro_de_produtos)

        self.lbl_qtfinal_imagem_pedidos = QLabel(self.widget_qtfinal_todas_opcoes)
        self.lbl_qtfinal_imagem_pedidos.setObjectName(u"lbl_qtfinal_imagem_pedidos")
        self.lbl_qtfinal_imagem_pedidos.setStyleSheet(u"image:url(:/icon/return_7835555.png)")

        self.horizontalLayout.addWidget(self.lbl_qtfinal_imagem_pedidos)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_qtfinal_cadastr_de_produtos = QPushButton(self.widget_qtfinal_todas_opcoes)
        self.btn_qtfinal_cadastr_de_produtos.setObjectName(u"btn_qtfinal_cadastr_de_produtos")

        self.horizontalLayout_2.addWidget(self.btn_qtfinal_cadastr_de_produtos)

        self.btn_qtfinal_pedidos = QPushButton(self.widget_qtfinal_todas_opcoes)
        self.btn_qtfinal_pedidos.setObjectName(u"btn_qtfinal_pedidos")

        self.horizontalLayout_2.addWidget(self.btn_qtfinal_pedidos)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl = QLabel(self.widget_qtfinal_todas_opcoes)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setStyleSheet(u"image:url(:/icon/shopping-cart_2331970.png)")

        self.horizontalLayout_4.addWidget(self.lbl)

        self.lbl_qtfinal_imagem_relatorios = QLabel(self.widget_qtfinal_todas_opcoes)
        self.lbl_qtfinal_imagem_relatorios.setObjectName(u"lbl_qtfinal_imagem_relatorios")
        self.lbl_qtfinal_imagem_relatorios.setStyleSheet(u"image: url(:/icon/data-analytics_9955699.png)")

        self.horizontalLayout_4.addWidget(self.lbl_qtfinal_imagem_relatorios)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_qtfinal_vendas = QPushButton(self.widget_qtfinal_todas_opcoes)
        self.btn_qtfinal_vendas.setObjectName(u"btn_qtfinal_vendas")

        self.horizontalLayout_3.addWidget(self.btn_qtfinal_vendas)

        self.btn_qtfinal_relatorios = QPushButton(self.widget_qtfinal_todas_opcoes)
        self.btn_qtfinal_relatorios.setObjectName(u"btn_qtfinal_relatorios")

        self.horizontalLayout_3.addWidget(self.btn_qtfinal_relatorios)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tb_qtfinal_estoque_baixo = QTableWidget(self.widget_qtfinal_todas_opcoes)
        if (self.tb_qtfinal_estoque_baixo.columnCount() < 2):
            self.tb_qtfinal_estoque_baixo.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_qtfinal_estoque_baixo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_qtfinal_estoque_baixo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_qtfinal_estoque_baixo.setObjectName(u"tb_qtfinal_estoque_baixo")
        self.tb_qtfinal_estoque_baixo.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_3.addWidget(self.tb_qtfinal_estoque_baixo)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.widget_qtfinal_todas_opcoes)

        janela_QTFinal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela_QTFinal)

        QMetaObject.connectSlotsByName(janela_QTFinal)
    # setupUi

    def retranslateUi(self, janela_QTFinal):
        janela_QTFinal.setWindowTitle(QCoreApplication.translate("janela_QTFinal", u"MainWindow", None))
        self.lbl_qtfinal_nome_gerenciamento_de_estoque.setText(QCoreApplication.translate("janela_QTFinal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Gerenciamento de estoque</span></p></body></html>", None))
        self.lbl_qtfinal_imagem_cadastro_de_produtos.setText("")
        self.lbl_qtfinal_imagem_pedidos.setText("")
        self.btn_qtfinal_cadastr_de_produtos.setText(QCoreApplication.translate("janela_QTFinal", u"Cadastrado de produtos", None))
        self.btn_qtfinal_pedidos.setText(QCoreApplication.translate("janela_QTFinal", u"Pedidos", None))
        self.lbl.setText("")
        self.lbl_qtfinal_imagem_relatorios.setText("")
        self.btn_qtfinal_vendas.setText(QCoreApplication.translate("janela_QTFinal", u"Vendas", None))
        self.btn_qtfinal_relatorios.setText(QCoreApplication.translate("janela_QTFinal", u"Relat\u00f3rios", None))
        ___qtablewidgetitem = self.tb_qtfinal_estoque_baixo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("janela_QTFinal", u"Produto", None));
        ___qtablewidgetitem1 = self.tb_qtfinal_estoque_baixo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("janela_QTFinal", u"Quantidade em estoque", None));
    # retranslateUi

