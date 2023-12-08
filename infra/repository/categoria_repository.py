from datetime import datetime
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.categoria import Categoria
from infra.entities.produto import Produto
from infra.entities.itensPedido import PedidoFornecedor

class CategoriaRepository:

    @staticmethod
    def select_categoria_by_id(id_categoria):
        with DBConnectionHandler() as db:
            return db.session.query(Categoria).filter(Categoria.id == id_categoria).first()

    @staticmethod
    def select_categoria_by_uniforme_id(id_categoria):
         with DBConnectionHandler() as db:
            return db.session.query(Categoria).filter(Categoria.id == id_categoria).first()

    @staticmethod
    def select_categoria_by_cpf(cpf_categoria):
        with DBConnectionHandler() as db:
            return db.session.query(Categoria).filter(Categoria.cpf == cpf_categoria).first()

    @staticmethod
    def select_all_categoria():
        with DBConnectionHandler() as db:
            return db.session.query(Categoria).all()

    @staticmethod
    def select_first_categoria():
        with DBConnectionHandler() as db:
            return db.session.query(Categoria).first()

    @staticmethod
    def insert_one_categoria(categoria):
        with DBConnectionHandler() as db:
            db.session.add(categoria)
            db.session.commit()

    @staticmethod
    def insert_many_categorias(categorias):
        with DBConnectionHandler() as db:
            db.session.add_all(categorias)
            db.session.commit()

    @staticmethod
    def update_categoria(categoria):
        with DBConnectionHandler() as db:
            db.session.query(categoria).filter(Categoria.id == categoria.id).update({'nome': categoria.nome, 'cpf': categoria.cpf})
            db.session.commit()

    @staticmethod
    def delete_categoria(categoria):
        with DBConnectionHandler() as db:
            db.session.query(categoria).filter(Categoria.id == categoria.id).update({'ativo': False})
            db.session.commit()

