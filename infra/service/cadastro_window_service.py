from datetime import datetime

import pandas
import pandas as pd
from PySide6.QtWidgets import QTableWidget, QMessageBox, QTableWidgetItem

from infra.repository.pedidoFornecedor_repository import PedidoFornecedorRepository
from infra.repository.produto_repository import ProdutoRepository


class CadastroWindowService:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.pedidoFornecedor_repository = PedidoFornecedorRepository()

