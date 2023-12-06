from __future__ import annotations

from enum import Enum
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from infra.config.base import Base


class StatusPedido(Enum):
    ABERTO = 'Aberto'
    FINALIZADO = 'Finalizado'


class ItensPedido (Base):
    __tablename__ = 'itens_pedido'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_do_pedido: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[StatusPedido] = mapped_column(nullable=False, default=StatusPedido.ABERTO)


    def __repr__(self):
        return f'PedidoFornecedor [data_do_pedido={self.data_do_pedido}, status={self.status}]'
