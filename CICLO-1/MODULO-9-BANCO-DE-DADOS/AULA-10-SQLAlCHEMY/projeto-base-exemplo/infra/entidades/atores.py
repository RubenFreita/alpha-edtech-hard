from infra.configuracoes.base import Base

# from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Atores(Base):
    __tablename__ = "atores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    filme_id: Mapped[str] = mapped_column(ForeignKey("filmes.id"), nullable=True)

    def __repr__(self):
        return f"Atores [id={self.id}, nome={self.nome}]"
