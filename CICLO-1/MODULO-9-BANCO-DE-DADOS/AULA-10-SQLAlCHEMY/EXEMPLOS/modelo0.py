from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base

# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#create-an-engine
# engine = create_engine('sqlite:///:memory:', echo=False)
# echo=True repete no console o comando em Python e depois equivalente em SQL
engine = create_engine(
    "sqlite:///C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-9-BANCO-DE-DADOS/AULA-10-SQLAlCHEMY/EXEMPLOS/pets.db",
    echo=True,
)

# class
Base = declarative_base()


class Pet(Base):
    # Tabela pets.db
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    petNome = Column(String)
    petIdade = Column(Integer)
    petTipo = Column(String)

    def __repr__(self):
        return f"{self.id} | {self.petNome} {self.petIdade} {self.petTipo}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
