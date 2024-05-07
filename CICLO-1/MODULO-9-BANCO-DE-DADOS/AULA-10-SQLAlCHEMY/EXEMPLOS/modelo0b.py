from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#create-an-engine
# engine = create_engine('sqlite:///:memory:', echo=True)
# echo=True repete no console o comando em Python e depois equivalente em SQL
engine = create_engine("sqlite:///pets.db", echo=True)

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
        return f"{self.id} | {self.petNome} | {self.petIdade} | {self.petTipo}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)

with Session(engine) as session:

    kika = Pet(id=1, petNome="Kika", petIdade=8, petTipo="Cachorro")

    session.add_all([kika])

    session.commit()

# print(kika)
# print(kika.id)
# print(kika.petNome)
# print(kika.petIdade)
# print(kika.petTipo)
# print("================")
# print()
