from infra.config.create_table import create_tables

from infra.config.conexao import DBConexaoManipulador
from infra.classes.cliente import Cliente
from infra.classes.lista_espera import ListaEspera
from infra.classes.mesa import Mesa
from infra.classes.mesa_reserva import MesaReserva

from infra.classes.reserva import Reserva
from datetime import date, time
from infra.repositorio.cliente_repositorio import ClienteRepositorio

create_tables()

with DBConexaoManipulador() as db:

    try:

        cliente1 = Cliente(
            None,
            "Ruben",
            "12345678",
            "98373641",
        )
        # cliente1 = Cliente(
        #     id=1,
        #     nome="Ruben",
        #     cpf="12345678",
        #     telefone="98373641",
        # )
        cliente2 = Cliente(id=2, nome="Daniel", cpf="43545678", telefone="98373231")

        mesa1 = Mesa(id=1, capacidade_pessoas=4)
        mesa2 = Mesa(id=2, capacidade_pessoas=4)
        mesa3 = Mesa(id=3, capacidade_pessoas=4)
        mesa4 = Mesa(id=4, capacidade_pessoas=6)

        reserva1 = Reserva(
            id=1,
            data_reserva=date(2024, 3, 17),
            horario_reserva=time(7, 30, 00),
            numero_pessoas=7,
            reserva_liberada=True,
            id_cliente=1,
        )
        reserva2 = Reserva(
            id=2,
            data_reserva=date(2024, 3, 16),
            horario_reserva=time(7, 00, 00),
            numero_pessoas=4,
            reserva_liberada=False,
            id_cliente=2,
        )
        # reserva1 = Reserva(
        #     id=1,
        #     data_reserva=date(2024, 3, 17),
        #     horario_reserva=time(7, 30, 00),
        #     numero_pessoas=7,
        #     reserva_liberada=True,
        #     # id_cliente=1,
        #     cliente=Cliente(id=1, nome="Ruben", cpf="12345678", telefone="98373641"),
        #     mesa_reserva=[
        #         MesaReserva(
        #             id=1, id_reserva=1, id_mesa=1, mesa=Mesa(id=1, capacidade_pessoas=4)
        #         ),
        #         MesaReserva(
        #             id=2, id_reserva=2, id_mesa=2, mesa=Mesa(id=2, capacidade_pessoas=4)
        #         ),
        #     ],
        # )
        # reserva2 = Reserva(
        #     id=2,
        #     data_reserva=date(2024, 3, 16),
        #     horario_reserva=time(7, 00, 00),
        #     numero_pessoas=4,
        #     reserva_liberada=False,
        #     # id_cliente=2,
        #     cliente=Cliente(id=2, nome="Daniel", cpf="43545678", telefone="98373231"),
        #     mesa_reserva=[],
        #     lista_espera=ListaEspera(id=1),
        # )

        mesa_reserva1 = MesaReserva(id=1, id_reserva=1, id_mesa=1)
        mesa_reserva2 = MesaReserva(id=2, id_reserva=2, id_mesa=2)

        lista_espera = ListaEspera(id=1, reserva_id=2)

        db.session.add_all(
            [
                cliente1,
                cliente2,
                mesa1,
                mesa2,
                mesa3,
                mesa4,
                reserva1,
                reserva2,
                mesa_reserva1,
                mesa_reserva2,
                lista_espera,
            ]
        )
        db.session.commit()

        # db.session.add_all([reserva1, reserva2])
    except Exception as e:
        print(e)
        db.session.rollback()

    repo = ClienteRepositorio()
    repo.update(nome_alvo="Ruben", nome="Artur", telefone="96035863")
    repo.insere(new_nome="Miguel", new_cpf="647389287", new_telefone="78909736")
    repo.delete(nome_alvo="Daniel")
    data = (
        db.session.query(MesaReserva)
        .join(Reserva)
        .join(Cliente)
        .join(Mesa)
        .with_entities(
            MesaReserva.id,
            Reserva.id,
            Reserva.data_reserva,
            Reserva.horario_reserva,
            Reserva.numero_pessoas,
            Reserva.reserva_liberada,
            Cliente.nome,
            Cliente.telefone,
            Mesa.capacidade_pessoas,
        )
        .filter(
            MesaReserva.id_reserva == Reserva.id,
        )
        .all()
    )

    for i in data:
        print(i)
