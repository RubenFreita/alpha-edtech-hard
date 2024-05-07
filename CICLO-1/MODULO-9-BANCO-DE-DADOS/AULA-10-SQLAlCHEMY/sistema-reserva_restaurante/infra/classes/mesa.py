from infra.config.base import Base
from infra.classes.mesa_reserva import MesaReserva
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Mesa(Base):
    __tablename__ = "mesas"

    id: Mapped[int] = mapped_column(primary_key=True)
    capacidade_pessoas: Mapped[int] = mapped_column(nullable=False)
    mesa_reserva: Mapped["MesaReserva"] = relationship(
        "MesaReserva",
        backref="mesa",
    )
