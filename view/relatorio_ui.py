# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogRelatorio.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_janela_relatorio(object):
    def setupUi(self, janela_relatorio):
        if not janela_relatorio.objectName():
            janela_relatorio.setObjectName(u"janela_relatorio")
        janela_relatorio.resize(400, 300)
        self.verticalLayout_4 = QVBoxLayout(janela_relatorio)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_relatorio_nome_relatorio = QLabel(janela_relatorio)
        self.lbl_relatorio_nome_relatorio.setObjectName(u"lbl_relatorio_nome_relatorio")

        self.verticalLayout_3.addWidget(self.lbl_relatorio_nome_relatorio)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_relatorio_nome_vendas_totais = QLabel(janela_relatorio)
        self.lbl_relatorio_nome_vendas_totais.setObjectName(u"lbl_relatorio_nome_vendas_totais")

        self.verticalLayout.addWidget(self.lbl_relatorio_nome_vendas_totais)

        self.tb_vendas_totais = QTableView(janela_relatorio)
        self.tb_vendas_totais.setObjectName(u"tb_vendas_totais")

        self.verticalLayout.addWidget(self.tb_vendas_totais)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_relatorio_nome_vendas_por_categoria = QLabel(janela_relatorio)
        self.lbl_relatorio_nome_vendas_por_categoria.setObjectName(u"lbl_relatorio_nome_vendas_por_categoria")

        self.verticalLayout_2.addWidget(self.lbl_relatorio_nome_vendas_por_categoria)

        self.tb_vendas_por_categoria = QTableView(janela_relatorio)
        self.tb_vendas_por_categoria.setObjectName(u"tb_vendas_por_categoria")

        self.verticalLayout_2.addWidget(self.tb_vendas_por_categoria)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(janela_relatorio)

        QMetaObject.connectSlotsByName(janela_relatorio)
    # setupUi

    def retranslateUi(self, janela_relatorio):
        janela_relatorio.setWindowTitle(QCoreApplication.translate("janela_relatorio", u"Dialog", None))
        self.lbl_relatorio_nome_relatorio.setText(QCoreApplication.translate("janela_relatorio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Relat\u00f3rios</span></p></body></html>", None))
        self.lbl_relatorio_nome_vendas_totais.setText(QCoreApplication.translate("janela_relatorio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vendas totais</span></p></body></html>", None))
        self.lbl_relatorio_nome_vendas_por_categoria.setText(QCoreApplication.translate("janela_relatorio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vendas por categoria</span></p></body></html>", None))
    # retranslateUi

