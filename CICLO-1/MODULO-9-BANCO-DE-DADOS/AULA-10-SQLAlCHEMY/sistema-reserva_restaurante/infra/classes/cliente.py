from typing import Any
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Index
from infra.config.base import Base
from infra.classes.reserva import Reserva


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False)
    telefone: Mapped[str] = mapped_column(nullable=False)
    reserva: Mapped["Reserva"] = relationship(
        "Reserva",
        backref="cliente",
    )
    __table_args__ = (
        Index("idx_id_cliente", "id"),
        Index("idx_nome_cliente", "nome"),
        Index("idx_cpf_cliente", "cpf"),
    )

    def __init__(self, id, nome, cpf, telefone, **kw: Any):
        super().__init__(**kw)
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
