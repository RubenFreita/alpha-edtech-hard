from infra.configuracoes.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infra.entidades.atores import Atores
from typing import List


class Filmes(Base):
    __tablename__ = "filmes"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    atores: Mapped[List["Atores"]] = relationship(
        "Atores", backref="atores", lazy="subquery"
    )

    def __repr__(self):
        return (
            f"Filme [titulo = {self.titulo}, genero = {self.genero}, ano = {self.ano}]"
        )
