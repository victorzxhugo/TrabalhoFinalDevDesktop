from datetime import datetime

import pandas
import pandas as pd
from PySide6.QtWidgets import QTableWidget, QMessageBox, QTableWidgetItem

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository


class MainWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.pedidoFornecedor_repository = PedidoFornecedorRepository()

    def populate_table_estoque_baixo(self, main_window):
        main_window.tb_qtfinal_estoque_baixo.setRowCount(0)
        lista_produtos = self.produto_repository.select_all_produtos()
        for produto in lista_produtos[:]:
            if produto.quantidade > 10:
                lista_produtos.remove(produto)
            main_window.tb_qtfinal_estoque_baixo.setRowCount(len(lista_produtos))
            for linha, produto in enumerate(lista_produtos):
                if produto.quantidade <= 5:
                    main_window.tb_qtfinal_estoque_baixo.setItem(linha, 0, QTableWidgetItem(produto.nome))
                    main_window.tb_qtfinal_estoque_baixo.setItem(linha, 1, QTableWidgetItem(produto.quantidade))

