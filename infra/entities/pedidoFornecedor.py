from __future__ import annotations
from typing import List
from sqlalchemy import ForeingKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from infra.config.base import Base


class StatusPedido(Enum):
    ABERTO = 'Aberto'
    FINALIZADO = 'Finalizado'


class PedidoFornecedor (Base):
    __tablename__ = 'pedido_fornecedor'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_do_pedido: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[StatusPedido] = mapped_column(nullable=False, default=StatusPedido.ABERTO)


    produtos: Mapped[List["Produto"]] = relationship("Produto",
                            cascade="all, delete", passives_deletes=False, lazy='joined')

    def __repr__(self):
        return f'PedidoFornecedor [data_do_pedido={self.data_do_pedido}, status={self.status}]'
