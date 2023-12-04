from PySide6.QtWidgets import QMessageBox

from infra.entities.produto import Produto
from infra.repository.produto_repository import ProdutoRepository
from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.service.cadastro_window_service import MainWindowService


class ProdutoService:
    def insert_Produto(self, cadastro_window):
        produto = Produto()
        produto.nome = cadastro_window.txt_cadastro_nome.text()
        produto.preco = cadastro_window.txt_cadastro_preco.text()
        produto.categoria_id = cadastro_window.selectedRow()

        try:
            self.produto_repository.insert_one_produto(produto)
            cadastro_window.text_nome_produto.setText('')
            self.service_cadastro_window.populate_table_produto(cadastro_window)
            QMessageBox.information(cadastro_window, 'produtos', f'produto cadastrado com sucesso')
        except Exception as e:
            QMessageBox.warning(cadastro_window, 'produtos', f'Erro ao cadastrar produto. \nErro: {e}')
