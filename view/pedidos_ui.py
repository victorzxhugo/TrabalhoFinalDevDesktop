# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogPedidos.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(564, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Pedidos</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Criar pedidos", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Produto", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Quantidade", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Finalizar pedido", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Receber pedidos", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Receber", None))
    # retranslateUi

