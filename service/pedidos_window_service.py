from PySide6.QtWidgets import QMessageBox

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository
from service.main_window_service import MainWindowService
from infra.entities.produto import Produto


class PedidosWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.pedidoFornecedor_repository = PedidoFornecedorRepository()
        self.main_window_service = MainWindowService()


    def buscar_produtos(self, pedidos_ui):
        pedidos_ui.comboBox_pedidos_produto.clear()
        txt_atual = pedidos_ui.txt_pedidos_produto.text()
        try:
            resultados = self.produto_repository.select_produto_search_name(txt_atual)
            self.lista_produtos = resultados
            if resultados is not None:
                for produto in resultados:
                    if produto.nome is not None:
                        pedidos_ui.comboBox_pedidos_produto.addItem(produto.nome)

                QMessageBox.information(pedidos_ui, 'Busca', 'Buscou com sucesso!')
        except Exception as e:
            QMessageBox.warning(pedidos_ui, 'Cadastroo', f'Erro ao cadastrar produto.\n Erro: {e}')




    def insert_pedido(self, pedidos_ui):
            if pedidos_ui.comboBox_pedidos_produto.currentText() != 'Selecione um item' and pedidos_ui.lista_produtos is not None:
                produto = self.produto_repository.select_uniforme_by_name(pedidos_ui.comboBox_pedidos_produto.currentText())

                try:
                    self.emprestimo_repository.insert_emprestimo(pedidos_ui.selected_funcionario, uniforme)
                    QMessageBox.information(pedidos_ui, 'Emprestimos', 'Empréstimo cadastrado com sucesso')
                except Exception as e:
                    QMessageBox.warning(pedidos_ui, 'Emprestimos', f'Erro ao cadastrar empréstimo cadastrado!\n Erro{e}')

            elif pedidos_ui.cb_tipo_uniforme.currentText() == 'Selecione um item' and pedidos_ui.selected_funcionario is not None:
                QMessageBox.warning(pedidos_ui, 'Emprestimos', f'Selecione um uniforme!')

            elif pedidos_ui.cb_tipo_uniforme.currentText() != 'Selecione um item' and pedidos_ui.selected_funcionario is None:
                QMessageBox.warning(pedidos_ui, 'Emprestimos', f'Selecione um funcionário!')

            else:
                QMessageBox.warning(pedidos_ui, 'Emprestimos', f'Selecione um funcionário e um uniforme!')
