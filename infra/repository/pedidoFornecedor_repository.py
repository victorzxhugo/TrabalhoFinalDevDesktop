from datetime import datetime
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.produto import Produto, Pedido, produto_pedido_association


class PedidoFornecedorRepository:

    @staticmethod
    def insert_many(produtos):
        with DBConnectionHandler() as db:
            try:
                # Criar um novo pedido
                novo_pedido = Pedido(data_do_pedido=datetime.now(), status='Aberto')
                db.session.add(novo_pedido)
                db.session.commit()

                # Associar os produtos ao novo pedido
                for produto_info in produtos:
                    print(produto_info['nome_produto'])
                    produto_existente = db.session.query(Produto).filter_by(nome=produto_info['nome_produto']).first()




                    # Verificar se o produto existe no banco de dados
                    if produto_existente:
                        insert_statement = produto_pedido_association.insert().values(produto_id=produto_existente.id,
                                                                   pedido_id=novo_pedido.id)

                        db.session.execute(insert_statement)
                        print("Inserindo produto_pedido_association:", produto_existente.id, novo_pedido.id)
                        db.session.commit()
                        print("Inserção concluída com sucesso.")

                    else:
                        print(f"Produto não encontrado: {produto_info['nome_produto']}")

            except Exception as e:
                print(e)

    @staticmethod
    def insert_pedido(produto):
        with DBConnectionHandler() as db:
            emp = Pedido()
            emp.produto_id = produto.id
            emp.status = 'Aberto'
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
                        db.update(Pedido(pedido_id=pedido.id, produto_id=produto.id, quantidade=produto.quantidade))

                pedido.status = 'Finalizado'
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_all_pedidos():
        with DBConnectionHandler() as db:
            pedidos = db.session.query(Pedido).all()
            return pedidos


    @staticmethod
    def select_pedidos_ativos():
        with DBConnectionHandler() as db:
            pedidos = (db.session.query(Pedido)
                .filter(PedidoFornecedor.status == 'Aberto')
                .all())
            return pedidos
