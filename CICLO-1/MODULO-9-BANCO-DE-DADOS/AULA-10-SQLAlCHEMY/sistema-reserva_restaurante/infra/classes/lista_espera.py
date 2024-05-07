from typing import Any
from infra.config.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from infra.config.conexao import DBConexaoManipulador

from infra.classes.reserva import Reserva


class ListaEspera(Base):
    __tablename__ = "lista_espera"

    id: Mapped[int] = mapped_column(primary_key=True)
    reserva_id: Mapped[int] = mapped_column(
        ForeignKey("reservas.id"),
    )

    # def __init__(self, id, reserva_id=None, **kw: Any):
    #     super().__init__(**kw)
    #     self.id = id
    #     with DBConexaoManipulador() as db:
    #         reserva = db.session.query(Reserva).filter(Reserva.id == reserva_id).all()
    #         if not reserva:
    #             print(
    #                 "====================================================================="
    #             )
    #             raise Exception("Erro: id_reserva não consta na tabela Reserva")
    #         self.reserva_id = reserva_id
    #         # flag = False
    # for reserva in reservas:
    #     if reserva.id != reserva_id:
    #         continue
    #     else:
    #         flag = True
    #         self.reserva_id = reserva_id

    # if flag == False:
    #     raise Exception("Erro: id_reserva não consta na tabela Reserva")
