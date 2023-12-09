import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPalette, QColor, Qt

from view.main_ui import Ui_janela_QTFinal
from view.relatorio_ui import Ui_janela_relatorio
from view.vendas_ui import Ui_janela_vendas
from view.pedidos_ui import Ui_janela_pedidos
from view.cadastro_ui import Ui_janela_cadastro
from service.cadastro_window_service import CadastroWindowService
from service.pedidos_window_service import PedidosWindowService
from infra.config.connection import DBConnectionHandler
from service.main_window_service import MainWindowService
class MainWindow(QMainWindow, Ui_janela_QTFinal, Ui_janela_cadastro):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_qtfinal_cadastr_de_produtos.clicked.connect(self.cadastrar_produtos)
        self.btn_qtfinal_pedidos.clicked.connect(self.pedidos)
        self.btn_qtfinal_vendas.clicked.connect(self.vendas)
        self.btn_qtfinal_relatorios.clicked.connect(self.relatorios)
        db = DBConnectionHandler()

        self.main_window_service = MainWindowService()

        self.main_window_service.populate_table_estoque_baixo(self)



    def cadastrar_produtos(self):
        self.cadastro_produto_dialog = CadastroDialog()
        self.cadastro_produto_dialog.show()



    def vendas(self):
        self.vendas_dialog = VendasDialog()
        self.vendas_dialog.show()

    def pedidos(self):
        self.pedidos_dialog = PedidosDialog()
        self.pedidos_dialog.show()

    def relatorios(self):
        self.relatorios_dialog = RelatorioDialog()
        self.relatorios_dialog.show()
class CadastroDialog(QDialog,Ui_janela_cadastro):
    def __init__(self, parent=None):
        super(CadastroDialog, self).__init__(parent)
        self.setupUi(self)
        self.cadastro_window_service = CadastroWindowService()
        self.btn_cadastro_cadastrar.clicked.connect(self.realizar_cadastro)

    def realizar_cadastro(self):
        self.cadastro_window_service.inserir_cadastro(self)

class VendasDialog(QDialog, Ui_janela_vendas):
    def __init__(self, parent=None):
        super(VendasDialog, self).__init__(parent)
        self.setupUi(self)

class RelatorioDialog(QDialog, Ui_janela_relatorio):
    def __init__(self, parent=None):
        super(RelatorioDialog, self).__init__(parent)
        self.setupUi(self)

class PedidosDialog(QDialog, Ui_janela_pedidos):
    def __init__(self, parent=None):
        super(PedidosDialog, self).__init__(parent)
        self.setupUi(self)
        self.lista_produtos = None
        self.pedidos_window_service = PedidosWindowService()
        self.btn_pedidos_buscar_produto.clicked.connect(self.buscar_produto_pedidos)
        self.btn_pedidos_buscar_produto.clicked.connect(self.adicionar_pedido_pedidos)
    def buscar_produto_pedidos(self):
        self.pedidos_window_service.buscar_produtos(self)
    def adicionar_pedido_pedidos(self):
        self.pedidos_window_service.insert_pedido(self)

if __name__ == "__main__":
    app = QApplication()

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
    app.setPalette(palette)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
