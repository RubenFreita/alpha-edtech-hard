from infra.config.base import Base
from infra.config.conexao import DBConexaoManipulador

from infra.classes.lista_espera import ListaEspera
from infra.classes.cliente import Cliente
from infra.classes.mesa import Mesa
from infra.classes.mesa_reserva import MesaReserva

from infra.classes.reserva import Reserva


def create_tables():
    with DBConexaoManipulador() as db:

        Base.metadata.create_all(db.get_engine())
