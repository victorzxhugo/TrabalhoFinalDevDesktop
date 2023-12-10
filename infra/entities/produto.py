from __future__ import annotations

from datetime import datetime

from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base
# from infra.entities.Produto_pedido import produto_pedido_association

produto_pedido_association = Table(
    'produto_pedido',
    Base.metadata,
    Column('produto_id', Integer, ForeignKey('produtos.id')),
    Column('pedido_id', Integer, ForeignKey('pedidos.id'))
)

class Produto (Base):
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False, unique=True)
    preco: Mapped[float] = mapped_column(nullable=False)
    quantidade: Mapped[int] = mapped_column(nullable=True)
    categoria: Mapped[str] = mapped_column(nullable=False)

    pedidos = relationship("Pedido", secondary=produto_pedido_association, back_populates="produtos")

    def __repr__(self):
        return f'Produto [nome={self.nome}, preco={self.preco}, quantidade_em_estoque={self.quantidade}]'


class Pedido (Base):
    __tablename__ = 'pedidos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_do_pedido: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)

    produtos: Mapped[list["Produto"]] = relationship( secondary=produto_pedido_association, back_populates="pedidos")

    def __repr__(self):
        return f'PedidoFornecedor [data_do_pedido={self.data_do_pedido}, status={self.status}]'



