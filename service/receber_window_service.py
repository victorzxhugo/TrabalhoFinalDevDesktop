from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository
from service.main_window_service import MainWindowService
from infra.entities.produto import Produto


class ReceberWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.pedidoFornecedor_repository = PedidoFornecedorRepository()
        self.main_window_service = MainWindowService()

    def populate_table_lista_receber(self, receber_ui):
        receber_ui.tb_receber_pedidos.setRowCount(0)

        pedidos = self.pedidoFornecedor_repository.select_all_pedidos()

        for linha, pedido in enumerate(pedidos):
            id_pedido = pedido.id
            data_pedido = pedido.data_do_pedido.strftime('%d-%m-%Y')
            status_pedido = pedido.status

            receber_ui.tb_receber_pedidos.insertRow(linha)
            receber_ui.tb_receber_pedidos.setItem(linha, 0, QTableWidgetItem(str(id_pedido)))
            receber_ui.tb_receber_pedidos.setItem(linha, 1, QTableWidgetItem(data_pedido))
            receber_ui.tb_receber_pedidos.setItem(linha, 2, QTableWidgetItem(status_pedido))

    def cancelar_recebimento(self, receber_ui):
        # Verificar se uma linha foi selecionada
        selected_row = receber_ui.tb_receber_pedidos.currentRow()

        if selected_row >= 0:
            id_pedido = int(receber_ui.tb_receber_pedidos.item(selected_row, 0).text())

            status_pedido = receber_ui.tb_receber_pedidos.item(selected_row, 2).text()

            if status_pedido == 'Aberto':
                pedido = self.pedidoFornecedor_repository.select_pedido_by_id(id_pedido)
                if pedido:
                    pedido.status = 'Cancelado'
                    self.pedidoFornecedor_repository.update_pedido_status(id_pedido, 'Cancelado')
                    self.populate_table_lista_receber(receber_ui)

                    QMessageBox.information(receber_ui, 'Pedido cancelado', 'Pedido cancelado com sucesso!')
                else:
                    QMessageBox.warning(receber_ui, 'Aviso', f'Pedido não encontrado para o ID {id_pedido}.')
            else:
                if status_pedido == 'Cancelado':
                    QMessageBox.warning(receber_ui, 'Aviso',
                                        f'O pedido já foi cancelado, portanto não pode ser cancelado novamente.')
                else:
                    QMessageBox.warning(receber_ui, 'Aviso',
                                    f'O pedido já foi recebido, portanto não pode ser cancelado.')
        else:
            QMessageBox.warning(receber_ui, 'Aviso', 'Selecione um pedido na tabela para cancelar o recebimento.')

    def visualizar_pedido_selecionado(self, visualizar_dialog, receber_ui):
        selected_row = receber_ui.tb_receber_pedidos.currentRow()

        if selected_row >= 0:
            id_pedido = int(receber_ui.tb_receber_pedidos.item(selected_row, 0).text())

            if id_pedido:
                self.populate_table_visualizar(visualizar_dialog.tb_visualizar_pedidos, id_pedido)
            else:
                QMessageBox.warning(receber_ui, 'Aviso', f'Pedido não encontrado para o ID {id_pedido}.')
        else:
            QMessageBox.warning(receber_ui, 'Aviso', 'Selecione um pedido na tabela para visualizar detalhes.')

    def populate_table_visualizar(self, tb_visualizar_pedidos, pedido_id):
        tb_visualizar_pedidos.setRowCount(0)

        produtos_quantidades = self.pedidoFornecedor_repository.select_produtos_quantidades_by_pedido_id(pedido_id)

        for produto, quantidade in produtos_quantidades:
            row_position = tb_visualizar_pedidos.rowCount()
            tb_visualizar_pedidos.insertRow(row_position)

            tb_visualizar_pedidos.setItem(row_position, 0, QTableWidgetItem(produto.nome))
            tb_visualizar_pedidos.setItem(row_position, 1, QTableWidgetItem(str(quantidade)))

    def finalizar_recebimento(self, receber_ui):
        selected_row = receber_ui.tb_receber_pedidos.currentRow()

        if selected_row >= 0:
            pedido_id = int(receber_ui.tb_receber_pedidos.item(selected_row, 0).text())
            status_pedido = receber_ui.tb_receber_pedidos.item(selected_row, 2).text()

            if status_pedido == 'Aberto':
                receber_ui.tb_receber_pedidos.setRowCount(0)

                produtos_quantidades = self.pedidoFornecedor_repository.select_produtos_quantidades_by_pedido_id(
                    pedido_id)

                for produto, quantidade in produtos_quantidades:
                    self.pedidoFornecedor_repository.update_quantidade_produto(produto.nome, quantidade)

                status = 'Recebido'
                self.pedidoFornecedor_repository.update_pedido_status(pedido_id, status)

                self.populate_table_lista_receber(receber_ui)

                QMessageBox.information(receber_ui, 'Recebimento concluído', 'Recebimento concluído com sucesso!')
            else:
                QMessageBox.warning(receber_ui, 'Aviso', 'O pedido só pode ser recebido se estiver "Aberto".')
        else:
            QMessageBox.warning(receber_ui, 'Aviso', 'Selecione um pedido na tabela para finalizar o recebimento.')
