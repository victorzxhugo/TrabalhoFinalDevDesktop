from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository
from service.main_window_service import MainWindowService
# from infra.entities.produto import Produto


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
        nome_produto = pedidos_ui.comboBox_pedidos_produto.currentText()
        quantidade_text = pedidos_ui.txt_pedidos_quantidade.text()

        if not nome_produto or not quantidade_text:
            QMessageBox.warning(pedidos_ui, 'Aviso', 'Por favor, preencha todos os campos.')
            return

        quantidade = int(quantidade_text)

        if nome_produto != 'Selecione um item' and quantidade > 0:
            if pedidos_ui.lista_produtos is None:
                pedidos_ui.lista_produtos = []
                informacoes_pedido = {'nome_produto': nome_produto, 'quantidade': quantidade}
                pedidos_ui.lista_produtos.append(informacoes_pedido)
                self.populate_table_lista_produtos(pedidos_ui)
            else:

                nomes_produtos = [produto['nome_produto'] for produto in pedidos_ui.lista_produtos]
                if nome_produto in nomes_produtos:
                    QMessageBox.warning(pedidos_ui, 'Aviso',
                                        f"Produto {nome_produto} já está na lista. Não é permitido duplicar produtos.")
                else:
                    informacoes_pedido = {'nome_produto': nome_produto, 'quantidade': quantidade}
                    pedidos_ui.lista_produtos.append(informacoes_pedido)
                    self.populate_table_lista_produtos(pedidos_ui)
                    print(f'Produto: {informacoes_pedido["nome_produto"]}, Quantidade: {informacoes_pedido["quantidade"]}')
        else:
            QMessageBox.warning(pedidos_ui, 'Aviso',
                                'Por favor, selecione um produto e preencha a quantidade corretamente.')


    def populate_table_lista_produtos(self, pedidos_ui):
        if pedidos_ui.lista_produtos is not None:

            pedidos_ui.tb_lista_produtos.setRowCount(0)

            for linha, produto_info in enumerate(pedidos_ui.lista_produtos):
                nome_produto = produto_info['nome_produto']
                quantidade = produto_info['quantidade']

                pedidos_ui.tb_lista_produtos.insertRow(linha)

                pedidos_ui.tb_lista_produtos.setItem(linha, 0, QTableWidgetItem(nome_produto))
                pedidos_ui.tb_lista_produtos.setItem(linha, 1, QTableWidgetItem(str(quantidade)))
        else:
            print(
                'A lista de produtos não foi inicializada. Certifique-se de inicializá-la antes de popular a tabela.')

    def remove_produto_selecionado(self, pedidos_ui):
        if pedidos_ui.lista_produtos is not None:
            selected_row = pedidos_ui.tb_lista_produtos.currentRow()

            if selected_row >= 0:
                nome_produto = pedidos_ui.tb_lista_produtos.item(selected_row, 0).text()

                for produto_info in pedidos_ui.lista_produtos:
                    if produto_info['nome_produto'] == nome_produto:
                        pedidos_ui.lista_produtos.remove(produto_info)

                self.populate_table_lista_produtos(pedidos_ui)
            else:
                QMessageBox.warning(pedidos_ui, 'Aviso', 'Selecione um produto na tabela para remover.')
        else:
            print('A lista de produtos não foi inicializada. Certifique-se de inicializá-la antes de remover itens.')

    def finalizar_pedido(self, pedidos_ui):
        if pedidos_ui.lista_produtos is not None and pedidos_ui.lista_produtos:
            try:

                self.pedidoFornecedor_repository.insert_many(pedidos_ui.lista_produtos)

                pedidos_ui.lista_produtos = []

                self.populate_table_lista_produtos(pedidos_ui)

                QMessageBox.information(pedidos_ui, 'Pedido Recebido', 'Pedido recebido com sucesso!')
            except Exception as e:
                QMessageBox.warning(pedidos_ui, 'Erro ao Finalizar Pedido', f'Erro ao finalizar pedido.\n Erro: {e}')
        else:
            QMessageBox.warning(pedidos_ui, 'Aviso',
                                'A lista de produtos está vazia. Adicione produtos antes de finalizar o pedido.')