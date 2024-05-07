from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import DeclarativeBase, relationship, Session
from datetime import date


class Base(DeclarativeBase):
    pass


class Aspirante(Base):
    __tablename__ = "aspirantes"
    id_aspirante = Column(Integer, primary_key=True)
    nome = Column(String(90))
    cpf = Column(String(13), unique=True)
    email = Column(String(90), unique=True)
    endereco = Column(String(120))
    aspirante_participante = relationship(
        "AspiranteParticipante", back_populates="aspirante"
    )


class AspiranteParticipante(Base):
    __tablename__ = "aspirantes_participantes"
    id_aspirante_participante = Column(Integer, primary_key=True)
    id_aspirantes_fk = Column(Integer, ForeignKey("aspirantes.id_aspirante"))
    id_desafios_fk = Column(Integer, ForeignKey("desafios.id_desafio"))
    id_equipe_fk = Column(Integer, ForeignKey("equipes.id_equipe"))
    nota_participante = Column(DECIMAL, server_default="0.0")
    aspirante = relationship(
        "Aspirante",
        back_populates="aspirante_participante",
    )
    desafio = relationship(
        "Desafio",
        back_populates="aspirante_participante",
    )
    equipe = relationship(
        "Equipe",
        back_populates="aspirante_participante",
    )


class Equipe(Base):
    __tablename__ = "equipes"
    id_equipe = Column(Integer, primary_key=True)
    id_aspirante_lider_fk = Column(
        Integer,
    )
    id_desafio_fk = Column(Integer, ForeignKey("desafios.id_desafio"))
    aspirante_participante = relationship(
        "AspiranteParticipante", back_populates="equipe"
    )
    desafio = relationship("Desafio", back_populates="equipe")


class Desafio(Base):
    __tablename__ = "desafios"
    id_desafio = Column(Integer, primary_key=True)
    titulo_desafio = Column(String(90))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    aspirante_participante = relationship(
        "AspiranteParticipante", back_populates="desafio"
    )
    equipe = relationship("Equipe", back_populates="desafio")


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-9-BANCO-DE-DADOS/AULA-10-SQLAlCHEMY/ATIVIDADE/Q02/env_q02/mini_desafio.db",
        echo=True,
    )

    # Criar as tabelas no banco de dados
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        aspirante1 = Aspirante(
            nome="Ruben",
            cpf="123.456.789-00",
            email="ruben@alpha.com",
            endereco="rua A, numero 2, bairro centro, Marco, Ceará",
        )
        aspirante2 = Aspirante(
            nome="João",
            cpf="123.456.789-01",
            email="joao@alpha.com",
            endereco="rua B, numero 2, bairro centro, Marco, Ceará",
        )
        aspirante3 = Aspirante(
            nome="Maria",
            cpf="123.456.712-00",
            email="maria@alpha.com",
            endereco="rua A, numero 6, bairro centro, Marco, Ceará",
        )
        aspirante4 = Aspirante(
            nome="Marcotti",
            cpf="321.456.712-00",
            email="marcotti@alpha.com",
            endereco="rua G, numero 6, bairro centro, Campinas, São Paulo",
        )
        aspirante5 = Aspirante(
            nome="Ana",
            cpf="124.654.712-00",
            email="ana@alpha.com",
            endereco="rua T, numero 1, bairro centro, Marco, Ceará",
        )

        desafio1 = Desafio(
            titulo_desafio="Mini Desafio",
            data_inicio=date(2024, 2, 5),
            data_fim=date(2024, 2, 10),
        )
        desafio2 = Desafio(
            titulo_desafio="Estrutura de dados",
            data_inicio=date(2024, 1, 5),
            data_fim=date(2024, 1, 15),
        )
        desafio3 = Desafio(
            titulo_desafio="Assincronismo",
            data_inicio=date(2024, 1, 5),
            data_fim=date(2024, 2, 1),
        )

        equipe1 = Equipe(
            id_aspirante_lider_fk=1,
            desafio=desafio1,
            aspirante_participante=[
                AspiranteParticipante(
                    desafio=desafio1,
                    aspirante=aspirante1,
                ),
                AspiranteParticipante(
                    desafio=desafio1,
                    aspirante=aspirante2,
                ),
            ],
        )
        equipe2 = Equipe(
            id_aspirante_lider_fk=3,
            desafio=desafio2,
            aspirante_participante=[
                AspiranteParticipante(
                    desafio=desafio2,
                    aspirante=aspirante3,
                ),
                AspiranteParticipante(
                    desafio=desafio2,
                    aspirante=aspirante4,
                ),
            ],
        )
        equipe3 = Equipe(
            id_aspirante_lider_fk=5,
            desafio=desafio3,
            aspirante_participante=[
                AspiranteParticipante(
                    desafio=desafio3,
                    aspirante=aspirante5,
                ),
            ],
        )

        session.add_all([equipe1, equipe2, equipe3])

        session.commit()
