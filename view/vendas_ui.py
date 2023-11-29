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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_produto_venda = QLineEdit(Dialog)
        self.txt_produto_venda.setObjectName(u"txt_produto_venda")

        self.horizontalLayout.addWidget(self.txt_produto_venda)

        self.btn_buscar_produto_venda = QPushButton(Dialog)
        self.btn_buscar_produto_venda.setObjectName(u"btn_buscar_produto_venda")

        self.horizontalLayout.addWidget(self.btn_buscar_produto_venda)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.comboBox_produto_venda = QComboBox(Dialog)
        self.comboBox_produto_venda.setObjectName(u"comboBox_produto_venda")

        self.verticalLayout.addWidget(self.comboBox_produto_venda)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txt_qtd_venda = QLineEdit(Dialog)
        self.txt_qtd_venda.setObjectName(u"txt_qtd_venda")

        self.verticalLayout.addWidget(self.txt_qtd_venda)

        self.btn_adicionar_venda = QPushButton(Dialog)
        self.btn_adicionar_venda.setObjectName(u"btn_adicionar_venda")

        self.verticalLayout.addWidget(self.btn_adicionar_venda)

        self.btn_finalizar_venda = QPushButton(Dialog)
        self.btn_finalizar_venda.setObjectName(u"btn_finalizar_venda")

        self.verticalLayout.addWidget(self.btn_finalizar_venda)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Vendas</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Produto", None))
        self.btn_buscar_produto_venda.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Quantidade", None))
        self.btn_adicionar_venda.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.btn_finalizar_venda.setText(QCoreApplication.translate("Dialog", u"Finalizar venda", None))
    # retranslateUi

