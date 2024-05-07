from infra.config.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, time


class MesaReserva(Base):
    __tablename__ = "mesa_reserva"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_reserva: Mapped[int] = mapped_column(ForeignKey("reservas.id"))
    id_mesa: Mapped[int] = mapped_column(ForeignKey("mesas.id"), nullable=True)
