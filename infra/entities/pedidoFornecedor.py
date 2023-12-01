from __future__ import annotations
from typing import List
from sqlalchemy import ForeingKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from infra.config.base import Base

class pedidoFornecedor (Base):
    __tablename__ = 'pedido_fornecedor'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_do_pedido: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)


    produtos: Mapped[List["Produto"]] = relationship("Produto",
                            cascade="all, delete", passives_deletes=False, lazy='joined')

    def __repr__(self):
        return f'PedidoFornecedor [data_do_pedido={self.data_do_pedido}, status={self.status}]'
