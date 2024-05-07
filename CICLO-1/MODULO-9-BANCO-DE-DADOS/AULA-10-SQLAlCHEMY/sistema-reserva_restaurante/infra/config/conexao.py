from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConexaoManipulador:
    def __init__(self) -> None:
        self.__string_conexao = "sqlite:///./reserva_restaurante.db"
        self.__engine = self.cria_conexao()
        self.session = None

    def cria_conexao(self):
        engine = create_engine(self.__string_conexao, echo=True)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session = sessionmaker(bind=self.__engine)
        self.session = session()
        return self

    def __exit__(self, a, b, c):
        self.session.close()
        print("fechando seção...")
