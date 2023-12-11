from datetime import datetime
from sqlalchemy.orm import joinedload, aliased

from infra.config.connection import DBConnectionHandler
from infra.entities.produto import Produto, Pedido, produto_pedido_association


class PedidoFornecedorRepository:

    @staticmethod
    def insert_many(produtos):
        with DBConnectionHandler() as db:
            try:

                novo_pedido = Pedido(data_do_pedido=datetime.now(), status='Aberto')
                db.session.add(novo_pedido)
                db.session.commit()


                for produto_info in produtos:
                    print(produto_info['nome_produto'])
                    produto_existente = db.session.query(Produto).filter_by(nome=produto_info['nome_produto']).first()


                    if produto_existente:
                        quantidade = produto_info['quantidade']

                        insert_statement = produto_pedido_association.insert().values(
                            produto_id=produto_existente.id,
                            pedido_id=novo_pedido.id,
                            quantidade=quantidade
                        )

                        db.session.execute(insert_statement)
                        print("Inserindo produto_pedido_association:", produto_existente.id, novo_pedido.id, quantidade)
                        db.session.commit()
                        print("Inserção concluída com sucesso.")
                    else:
                        print(f"Produto não encontrado: {produto_info['nome_produto']}")

            except Exception as e:
                print(e)

    def select_pedido_by_id(self, pedido_id):
        with DBConnectionHandler() as db:
            try:
                pedido = db.session.query(Pedido).filter(Pedido.id == pedido_id).first()
                return pedido
            except Exception as e:
                print(e)

    def select_all_pedidos(self):
        with DBConnectionHandler() as db:
            pedidos = db.session.query(Pedido).all()
            return pedidos

    @staticmethod
    def update_pedido_status(id_pedido, novo_status):
        with DBConnectionHandler() as db:
            try:
                pedido = db.session.query(Pedido).filter_by(id=id_pedido).first()

                if pedido:

                    pedido.status = novo_status

                    db.session.commit()
                    print(f"Status do Pedido {pedido.id} atualizado para {novo_status}")
                else:
                    print(f"Pedido com id {pedido.id} não encontrado.")
            except Exception as e:
                print(f"Erro ao atualizar status do pedido {pedido.id}. Erro: {e}")


    def select_produtos_quantidades_by_pedido_id(self, pedido_id):
        with DBConnectionHandler() as db:
            try:
                ProdutoAlias = aliased(Produto)
                result = (db.session.query(ProdutoAlias, produto_pedido_association.c.quantidade)
                    .join(produto_pedido_association, ProdutoAlias.id == produto_pedido_association.c.produto_id)
                    .filter(produto_pedido_association.c.pedido_id == pedido_id)
                    .all())

                return result
            except Exception as e:
                print(e)


    def update_quantidade_produto(self, nome_produto, quantidade_adicional):
        with DBConnectionHandler() as db:
            try:
                print(nome_produto, quantidade_adicional)

                produto = db.session.query(Produto).filter_by(nome=nome_produto).first()

                if produto:
                    if produto.quantidade is None:
                        produto.quantidade = quantidade_adicional
                    else:
                        produto.quantidade += quantidade_adicional

                    db.session.commit()
                    print(f"Quantidade do produto {nome_produto} atualizada para {produto.quantidade}")
                else:
                    print(f"Produto {nome_produto} não encontrado.")
            except Exception as e:
                print(f"Erro ao atualizar a quantidade do produto {nome_produto}: {e}")









