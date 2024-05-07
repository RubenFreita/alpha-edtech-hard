from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import dotenv as dt

# Carregar variáveis de ambiente
dt.load_dotenv()


class DBManipuladorConexao:
    def __init__(self) -> None:
        self.__conexao_string = os.getenv("URL_SQLITE")
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__conexao_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session = sessionmaker(bind=self.__engine)
        self.session = session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
