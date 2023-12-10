# from __future__ import annotations
#
# from enum import Enum
# from typing import List
# from sqlalchemy import ForeignKey, Table, Column
# from sqlalchemy.orm import relationship, Mapped, mapped_column
# from datetime import datetime
# from infra.config.base import Base
# from infra.entities.Produto_pedido import produto_pedido_association
#
#
#
# class Pedido (Base):
#     __tablename__ = 'pedidos'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     data_do_pedido: Mapped[datetime] = mapped_column(nullable=False)
#     status: Mapped[str] = mapped_column(nullable=False)
#
#     produtos: Mapped[list["Produto"]] = relationship( secondary=produto_pedido_association, back_populates="produtos",
#                cascade="all, delete-orphan")
#
#     def __repr__(self):
#         return f'PedidoFornecedor [data_do_pedido={self.data_do_pedido}, status={self.status}]'