from infra.config.base import Base
from infra.classes.mesa_reserva import MesaReserva

# from infra.classes.lista_espera import ListaEspera
from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, time
from typing import List


class Reserva(Base):

    __tablename__ = "reservas"

    id: Mapped[int] = mapped_column(primary_key=True)
    data_reserva: Mapped[date] = mapped_column(nullable=False)
    horario_reserva: Mapped[time] = mapped_column(nullable=False)
    numero_pessoas: Mapped[int] = mapped_column(nullable=False)
    reserva_liberada: Mapped[int] = mapped_column(nullable=False)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    mesa_reserva: Mapped[List["MesaReserva"]] = relationship(
        "MesaReserva",
        backref="reserva",
    )
    lista_espera = relationship(
        "ListaEspera",
        backref="reserva",
    )

    __table_args__ = (
        Index("idx_id_reserva", "id"),
        Index("idx_data_reserva", "data_reserva"),
        Index("idx_horario_reserva", "horario_reserva"),
        Index("idx_reserva_liberada", "reserva_liberada"),
    )
