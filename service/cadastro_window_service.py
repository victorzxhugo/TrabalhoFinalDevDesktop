from PySide6.QtWidgets import QMessageBox

from infra.repository.produto_repository import ProdutoRepository
from service.main_window_service import MainWindowService
from infra.entities.produto import Produto


class CadastroWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        # self.pedidoFornecedor_repository = PedidoFornecedorRepository()
        self.main_window_service = MainWindowService()

    def inserir_cadastro(self, cadastro_ui):
        produto = Produto()
        produto.nome = cadastro_ui.txt_cadastro_nome.text()
        produto.preco = cadastro_ui.txt_cadastro_preco.text()
        produto.quantidade = 0

        if self.produto_repository.select_produto_by_name(produto.nome) == False:
            if produto.nome and produto.preco and cadastro_ui.comboBox_cadastro_categoria.currentText() != 'Selecione um item':
                produto.preco = produto.preco.replace('.', '').replace(',', '.')
                try:
                    produto.preco = float(produto.preco)
                    produto.categoria = cadastro_ui.comboBox_cadastro_categoria.currentText()
                    self.produto_repository.insert_one_produto(produto)
                    QMessageBox.information(cadastro_ui, 'Cadastro', 'Cadastrado com sucesso!')
                except ValueError as e:
                    QMessageBox.warning(cadastro_ui, 'Cadastro', 'O campo de preço deve conter apenas números válidos.')
                except Exception as e:
                    QMessageBox.warning(cadastro_ui, 'Cadastro', f'Erro ao cadastrar produto.\nErro: {e}')
            else:
                QMessageBox.warning(cadastro_ui, 'Cadastro', 'Por favor, preencha todos os campos obrigatórios.')
        else:
            QMessageBox.warning(cadastro_ui, 'Cadastro', 'Esse produto já existe.')

