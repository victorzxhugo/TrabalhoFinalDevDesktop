from datetime import datetime

from pandas.io.formats import console
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.produto import Produto

class ProdutoRepository:


    @staticmethod
    def select_produto_by_id(id_produto):
        with DBConnectionHandler() as db :
            return db.session.query(Produto).filter(Produto.id == id_produto).first()


    @staticmethod
    def select_produto_by_name(name_produto):
        with DBConnectionHandler() as db :
            return db.session.query(Produto).filter( Produto.nome.like(name_produto) and Produto.categoria.like(name_produto)).first()
    @staticmethod
    def select_produto_search_name(name_produto):
          with DBConnectionHandler() as db:
            return db.session.query(Produto).filter(Produto.nome.contains(name_produto)).all()

    @staticmethod
    def select_all_produtos():
        with DBConnectionHandler() as db :
            return db.session.query(Produto).all()


    @staticmethod
    def select_first_produto():
        with DBConnectionHandler() as db :
            return db.session.query(Produto).first()

    @staticmethod
    def insert_many_produtos(produtos):
        with DBConnectionHandler() as db :
            if isinstance(produtos, list):
                db.session.query(Produto).add_all(produtos)
                db.session.commit()
            else:
                print(produtos)

    @staticmethod
    def insert_one_produto(produto):
        with DBConnectionHandler() as db :
            db.session.add(produto)
            db.session.commit()

    @staticmethod
    def update_produto(produto):
        with DBConnectionHandler() as db :
            db.session.query(Produto).filter(Produto.id == produto.id).update({'nome': produto.nome})
            db.session.commit()

    @staticmethod
    def delete_produto(produto):
        with DBConnectionHandler() as db :
            db.session.query(Produto).filter(produto.id == produto.id).update({'ativo': False})
            db.session.commit()
