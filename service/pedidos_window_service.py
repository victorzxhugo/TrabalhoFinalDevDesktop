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

        if nome_produto != 'Selecione um item' and pedidos_ui.txt_pedidos_quantidade.text():

            quantidade = int(pedidos_ui.txt_pedidos_quantidade.text())
            informacoes_pedido = {'nome_produto': nome_produto, 'quantidade': quantidade}
            if pedidos_ui.lista_produtos is None:
                pedidos_ui.lista_produtos = []
                pedidos_ui.lista_produtos.append(informacoes_pedido)
                print(f'Produto: {informacoes_pedido["nome_produto"]}, Quantidade: {informacoes_pedido["quantidade"]}')
                self.populate_table_lista_produtos(pedidos_ui)
            else:
                pedidos_ui.lista_produtos.append(informacoes_pedido)
                self.populate_table_lista_produtos(pedidos_ui)
                print(f'Produto: {informacoes_pedido["nome_produto"]}, Quantidade: {informacoes_pedido["quantidade"]}')

        else:

            print('Por favor, selecione um produto e preencha a quantidade.')


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
        # Verificar se a lista_produtos não é nula
        if pedidos_ui.lista_produtos is not None:
            # Obter a linha selecionada na tabela
            selected_row = pedidos_ui.tb_lista_produtos.currentRow()

            # Verificar se uma linha foi realmente selecionada
            if selected_row >= 0:
                # Obter o nome do produto na linha selecionada
                nome_produto = pedidos_ui.tb_lista_produtos.item(selected_row, 0).text()

                # Remover o produto correspondente da lista
                for produto_info in pedidos_ui.lista_produtos:
                    if produto_info['nome_produto'] == nome_produto:
                        pedidos_ui.lista_produtos.remove(produto_info)
                        break  # Assumindo que não há duplicatas de nomes de produtos

                # Atualizar a tabela após remover o produto
                self.populate_table_lista_produtos(pedidos_ui)
            else:
                # Nenhuma linha foi selecionada
                QMessageBox.warning(pedidos_ui, 'Aviso', 'Selecione um produto na tabela para remover.')
        else:
            # Adicionar lógica para lidar com o caso em que lista_produtos é nula
            print('A lista de produtos não foi inicializada. Certifique-se de inicializá-la antes de remover itens.')

    def finalizar_pedido(self, pedidos_ui):
        if pedidos_ui.lista_produtos is not None and pedidos_ui.lista_produtos:
            try:

                self.pedidoFornecedor_repository.insert_many(pedidos_ui.lista_produtos)

                # Limpar a lista_produtos após finalizar o pedido
                pedidos_ui.lista_produtos = []

                # Atualizar a tabela após finalizar o pedido
                self.populate_table_lista_produtos(pedidos_ui)

                QMessageBox.information(pedidos_ui, 'Pedido Finalizado', 'Pedido finalizado com sucesso!')
            except Exception as e:
                QMessageBox.warning(pedidos_ui, 'Erro ao Finalizar Pedido', f'Erro ao finalizar pedido.\n Erro: {e}')
        else:
            QMessageBox.warning(pedidos_ui, 'Aviso',
                                'A lista de produtos está vazia. Adicione produtos antes de finalizar o pedido.')