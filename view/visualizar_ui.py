# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogVisualizar.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_janela_visualizar(object):
    def setupUi(self, janela_visualizar):
        if not janela_visualizar.objectName():
            janela_visualizar.setObjectName(u"janela_visualizar")
        janela_visualizar.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(janela_visualizar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_visualizar_pedidos = QLabel(janela_visualizar)
        self.lbl_visualizar_pedidos.setObjectName(u"lbl_visualizar_pedidos")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_visualizar_pedidos.setFont(font)
        self.lbl_visualizar_pedidos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_visualizar_pedidos)

        self.tb_visualizar_pedidos = QTableWidget(janela_visualizar)
        if (self.tb_visualizar_pedidos.columnCount() < 2):
            self.tb_visualizar_pedidos.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_visualizar_pedidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_visualizar_pedidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_visualizar_pedidos.setObjectName(u"tb_visualizar_pedidos")
        self.tb_visualizar_pedidos.verticalHeader().hide()
        self.tb_visualizar_pedidos.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_visualizar_pedidos.setEditTriggers(QTableWidget.NoEditTriggers)

        self.verticalLayout_2.addWidget(self.tb_visualizar_pedidos)


        self.retranslateUi(janela_visualizar)

        QMetaObject.connectSlotsByName(janela_visualizar)
    # setupUi

    def retranslateUi(self, janela_visualizar):
        janela_visualizar.setWindowTitle(QCoreApplication.translate("janela_visualizar", u"Dialog", None))
        self.lbl_visualizar_pedidos.setText(QCoreApplication.translate("janela_visualizar", u"Visualizar Produtos do Pedido", None))
        ___qtablewidgetitem = self.tb_visualizar_pedidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("janela_visualizar", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_visualizar_pedidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("janela_visualizar", u"Quantidade", None));
    # retranslateUi

