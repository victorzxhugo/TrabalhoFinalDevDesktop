from __future__ import annotations
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


from infra.config.base import Base

class Produto (Base):
    __tablename__ = 'produto'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)
    quantidade: Mapped[int] = mapped_column(nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categoria.id", ondelete="CASCADE"))
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedido.id", ondelete="CASCADE"))

    def __repr__(self):
        return f'Produto [nome={self.nome}, preco={self.preco}, quantidade_em_estoque={self.quantidade_em_estoque}]'
