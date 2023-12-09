# from __future__ import annotations
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship, Mapped, mapped_column
#
#
#
# class PedidosAbertos:
#     __tablename__ = 'pedidos_abertos'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     itens_pedido_id: Mapped[int] = mapped_column(ForeignKey('itensPedido.id'))
#     produtos_id: Mapped[int] = mapped_column(ForeignKey('Produto.id'))
#
#     produto = relationship("Produto", back_populates="pedidos_abertos")
#     itens_pedido = relationship("ItensPedido", back_populates="pedidos_abertos")
