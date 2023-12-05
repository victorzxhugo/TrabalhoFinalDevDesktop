from datetime import datetime

import pandas
import pandas as pd
from PySide6.QtWidgets import QTableWidget, QMessageBox, QTableWidgetItem

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository
from infra.service.main_window_service import MainWindowService
from infra.entities.produto import Produto


class CadastroWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.pedidoFornecedor_repository = PedidoFornecedorRepository()
        self.main_window_service = MainWindowService()

    def inserir_cadastro(self, cadastro_ui):
        produto = Produto()
        produto.nome = cadastro_ui.txt_cadastro_nome.text()
        produto.preco = cadastro_ui.txt_cadastro_preco.text()
        if cadastro_ui.comboBox_cadastro_categoria.currentText() != 'Selecione um item':
            produto.categoria = cadastro_ui.comboBox_cadastro_categoria.currentText()
            try:
                self.produto_repository.insert_one_produto(produto)
                QMessageBox.information(cadastro_ui, 'Cadastro', 'Cadastrado com sucesso!')
            except Exception as e:
                QMessageBox.warning(cadastro_ui, 'Cadastroo', f'Erro ao cadastrar produto.\n Erro: {e}')

