from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


class DBConexaoManipulador:
    def __init__(self) -> None:
        self.__string_conexao = "sqlite:///./db_plataforma_comunicacao.db"
        self.__engine = self.create_database_engine()
        self.session = None

    def create_database_engine(self):
        return create_engine(self.__string_conexao, echo=True)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session = sessionmaker(bind=self.__engine)
        self.session = session()
        return self

    def __exit__(self, a, b, c):
        self.session.close()
