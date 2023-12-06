from datetime import datetime
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.produto import Produto
from infra.entities.itensPedido import ItensPedido, StatusPedido


class PedidoFornecedorRepository:

    @staticmethod
    def insert_pedido(produto):
        with DBConnectionHandler() as db:
            emp = PedidoFornecedor()
            emp.produto_id = produto.id
            emp.status = StatusPedido.ABERTO
            today = datetime.now()
            emp.data_emprestimo = today

            try:
                db.session.add(emp)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def finalize_pedido(pedido):
        with DBConnectionHandler() as db:
            try:
                if pedido:
                    for produto in pedido.produtos:
                        db.update(PedidoFornecedor(pedido_id=pedido.id, produto_id=produto.id, quantidade=produto.quantidade))

                pedido.status = StatusPedido.FINALIZADO
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_all_pedidos():
        with DBConnectionHandler() as db:
            pedidos = db.session.query(PedidoFornecedor).all()
            return pedidos


    @staticmethod
    def select_pedidos_ativos():
        with DBConnectionHandler() as db:
            pedidos = (db.session.query(PedidoFornecedor)
                .filter(PedidoFornecedor.status == StatusPedido.ABERTO)
                .all())
            return pedidos
