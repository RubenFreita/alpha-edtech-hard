from infra.config.conexao import DBConexaoManipulador
from infra.classes.reserva import Reserva


class ClienteRepositorio:

    def insere(
        self,
        new_data_reserva,
        new_horario_reserva,
        new_cliente,
        new_mesa_reserva,
        new_id=None,
    ):
        with DBConexaoManipulador() as db:
            db.session.add(Reserva(id=new_id))
