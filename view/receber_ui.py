# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogReceber.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_janela_receber(object):
    def setupUi(self, janela_receber):
        if not janela_receber.objectName():
            janela_receber.setObjectName(u"janela_receber")
        janela_receber.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(janela_receber)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_receber_pedidos = QLabel(janela_receber)
        self.lbl_receber_pedidos.setObjectName(u"lbl_receber_pedidos")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_receber_pedidos.setFont(font)
        self.lbl_receber_pedidos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_receber_pedidos)

        self.tb_receber_pedidos = QTableWidget(janela_receber)
        if (self.tb_receber_pedidos.columnCount() < 3):
            self.tb_receber_pedidos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_receber_pedidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_receber_pedidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_receber_pedidos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_receber_pedidos.setObjectName(u"tb_receber_pedidos")

        self.verticalLayout_2.addWidget(self.tb_receber_pedidos)

        self.btn_visualizar = QPushButton(janela_receber)
        self.btn_visualizar.setObjectName(u"btn_visualizar")

        self.verticalLayout_2.addWidget(self.btn_visualizar)

        self.btn_cancelar = QPushButton(janela_receber)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.verticalLayout_2.addWidget(self.btn_cancelar)

        self.btn_receber = QPushButton(janela_receber)
        self.btn_receber.setObjectName(u"btn_receber")

        self.verticalLayout_2.addWidget(self.btn_receber)


        self.retranslateUi(janela_receber)

        QMetaObject.connectSlotsByName(janela_receber)
    # setupUi

    def retranslateUi(self, janela_receber):
        janela_receber.setWindowTitle(QCoreApplication.translate("janela_receber", u"Dialog", None))
        self.lbl_receber_pedidos.setText(QCoreApplication.translate("janela_receber", u"Receber pedidos", None))
        ___qtablewidgetitem = self.tb_receber_pedidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("janela_receber", u"Id", None));
        ___qtablewidgetitem1 = self.tb_receber_pedidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("janela_receber", u"Data", None));
        ___qtablewidgetitem2 = self.tb_receber_pedidos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("janela_receber", u"Status", None));
        self.btn_visualizar.setText(QCoreApplication.translate("janela_receber", u"Visualizar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("janela_receber", u"Cancelar", None))
        self.btn_receber.setText(QCoreApplication.translate("janela_receber", u"Receber", None))
    # retranslateUi

