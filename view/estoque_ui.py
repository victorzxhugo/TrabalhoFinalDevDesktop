# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDialogEstoque.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_janela_estoque(object):
    def setupUi(self, janela_estoque):
        if not janela_estoque.objectName():
            janela_estoque.setObjectName(u"janela_estoque")
        janela_estoque.resize(400, 307)
        self.verticalLayout_4 = QVBoxLayout(janela_estoque)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_estoque = QLabel(janela_estoque)
        self.lbl_estoque.setObjectName(u"lbl_estoque")

        self.verticalLayout_3.addWidget(self.lbl_estoque)

        self.label = QLabel(janela_estoque)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.combobox_categorias = QComboBox(janela_estoque)
        self.combobox_categorias.setObjectName(u"combobox_categorias")
        self.combobox_categorias.addItem('Todas')
        self.combobox_categorias.addItem('Bebidas')
        self.combobox_categorias.addItem('Comida')
        self.combobox_categorias.addItem('Padaria')

        self.verticalLayout_3.addWidget(self.combobox_categorias)

        self.btn_buscar = QPushButton(janela_estoque)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.verticalLayout_3.addWidget(self.btn_buscar)

        self.tb_estoque = QTableWidget(janela_estoque)
        if (self.tb_estoque.columnCount() < 4):
            self.tb_estoque.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_estoque.setObjectName(u"tb_estoque")
        self.tb_estoque.verticalHeader().hide()
        self.tb_estoque.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_estoque.setEditTriggers(QTableWidget.NoEditTriggers)
        self.verticalLayout_3.addWidget(self.tb_estoque)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(janela_estoque)

        QMetaObject.connectSlotsByName(janela_estoque)
    # setupUi

    def retranslateUi(self, janela_estoque):
        janela_estoque.setWindowTitle(QCoreApplication.translate("janela_estoque", u"Dialog", None))
        self.lbl_estoque.setText(QCoreApplication.translate("janela_estoque", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Estoque</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("janela_estoque", u"Selecione uma categoria", None))
        self.btn_buscar.setText(QCoreApplication.translate("janela_estoque", u"Buscar", None))
        ___qtablewidgetitem = self.tb_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("janela_estoque", u"Id", None));
        ___qtablewidgetitem1 = self.tb_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("janela_estoque", u"Nome", None));
        ___qtablewidgetitem2 = self.tb_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("janela_estoque", u"Quantidade", None));
        ___qtablewidgetitem3 = self.tb_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("janela_estoque", u"Pre\u00e7o", None));
    # retranslateUi

