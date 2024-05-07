from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConexaoManipulador:
    def __init__(self) -> None:
        self.__string_conexao_banco = "sqlite:///./sistema_restaurante.db"
        self.__engine = self.create_database_engine()
        self.session = None

    def create_database_engine(self):
        return create_engine(self.__string_conexao_banco, echo=True)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session = sessionmaker(bind=self.__engine)
        self.session = session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
