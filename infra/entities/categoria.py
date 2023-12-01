from __future__ import annotations
from sqlalchemy import ForeingKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from infra.config.base import Base

class Categoria (Base):
    __tablename__ = 'categoria'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)

    produtos: Mapped[List["Produto"]] = relationship("Produto",
                    cascade="all, delete", passives_deletes=False, lazy='joined')

    def __repr__(self):
        return f'Categoria [nome_da_categoria={self.nome_da_categoria}]'

