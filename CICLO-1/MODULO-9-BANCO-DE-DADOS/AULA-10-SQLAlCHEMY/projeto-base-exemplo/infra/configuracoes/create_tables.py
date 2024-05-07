from infra.configuracoes.base import Base
from infra.configuracoes.conexao import DBManipuladorConexao

from infra.entidades.filmes import Filmes
from infra.entidades.atores import Atores


def create_tables():
    with DBManipuladorConexao() as db:
        Base.metadata.create_all(db.get_engine())
        # db.get
