from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository
from service.main_window_service import MainWindowService
from infra.entities.produto import Produto


class EstoqueWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.pedidoFornecedor_repository = PedidoFornecedorRepository()
        self.main_window_service = MainWindowService()

    def buscar_produtos(self, estoque_ui):
        categoria = estoque_ui.combobox_categorias.currentText()

        try:
            if categoria == 'Todas':
                produtos = self.produto_repository.select_all_produtos()
            else:
                produtos = self.produto_repository.select_by_categorias(categoria)

            self.populate_table_estoque(estoque_ui, produtos)

            QMessageBox.information(estoque_ui, 'Estoque!', 'Busca efetuada!')
        except Exception as e:
            QMessageBox.warning(estoque_ui, 'Estoque', f'Erro ao buscar.\n Erro: {e}')

    def populate_table_estoque(self, estoque_ui, produtos):
        estoque_ui.tb_estoque.setRowCount(0)
        for produto in produtos:
            row_position = estoque_ui.tb_estoque.rowCount()
            estoque_ui.tb_estoque.insertRow(row_position)

            estoque_ui.tb_estoque.setItem(row_position, 0, QTableWidgetItem(str(produto.id)))
            estoque_ui.tb_estoque.setItem(row_position, 1, QTableWidgetItem(produto.nome))
            estoque_ui.tb_estoque.setItem(row_position, 2, QTableWidgetItem(str(produto.quantidade)))
            estoque_ui.tb_estoque.setItem(row_position, 3, QTableWidgetItem(str(produto.preco)))


