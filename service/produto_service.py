from PySide6.QtWidgets import QMessageBox

from infra.entities.produto import Produto
from infra.repository.produto_repository import ProdutoRepository
from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository



class ProdutoService:
    def insert_Produto(self, cadastro_ui):
        produto = Produto()
        produto.nome = cadastro_ui.txt_cadastro_nome.text()
        produto.preco = cadastro_ui.txt_cadastro_preco.text()
        produto.categoria_id = cadastro_ui.selectedRow()

        try:
            self.produto_repository.insert_one_produto(produto)
            cadastro_ui.txt_cadastro_nome.setText('')
            cadastro_ui.txt_cadastro_preco.setText('')
            self.service_cadastro_ui.populate_table_produto(cadastro_ui)
            QMessageBox.information(cadastro_ui, 'produtos', f'produto cadastrado com sucesso')
        except Exception as e:
            QMessageBox.warning(cadastro_ui, 'produtos', f'Erro ao cadastrar produto. \nErro: {e}')
