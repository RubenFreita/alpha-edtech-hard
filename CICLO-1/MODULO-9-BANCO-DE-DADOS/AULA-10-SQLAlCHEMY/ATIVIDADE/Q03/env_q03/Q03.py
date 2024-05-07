from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    DECIMAL,
    Date,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, relationship, Session
from datetime import date


class Base(DeclarativeBase):
    pass


class Cor(Base):
    __tablename__ = "cores"
    id_cor = Column(Integer, primary_key=True)
    nome_cor = Column(String(20))
    veiculo = relationship("Veiculo", back_populates="cor")


class Veiculo(Base):
    __tablename__ = "veiculos"
    id_veiculo = Column(Integer, primary_key=True)
    veiculo_descricao = Column(Text)
    veiculo_placa = Column(String(7))
    id_cor_fk = Column(Integer, ForeignKey("cores.id_cor"))
    cor = relationship("Cor", back_populates="veiculo")
    motorista = relationship("Motorista", back_populates="veiculo")
    viagem = relationship(
        "Viagem",
        back_populates="veiculo",
    )


class Motorista(Base):
    __tablename__ = "motoristas"
    id_motorista = Column(Integer, primary_key=True)
    nome_motorista = Column(String(90))
    nota_motorista = Column(DECIMAL)
    id_veiculo_fk = Column(Integer, ForeignKey("veiculos.id_veiculo"))
    veiculo = relationship("Veiculo", back_populates="motorista")
    viagem = relationship("Viagem", back_populates="motorista")


class Viagem(Base):
    __tablename__ = "viagens"
    id_viagem = Column(Integer, primary_key=True)
    viagem_origem = Column(String(90))
    viagem_destino = Column(String(90))
    viagem_partida = Column(Date)
    viagem_chegada = Column(Date)
    viagem_duracao = Column(Integer)
    id_motorista_fk = Column(Integer, ForeignKey("motoristas.id_motorista"))
    id_veiculo_fk = Column(Integer, ForeignKey("veiculos.id_veiculo"))
    id_passageiro_fk = Column(Integer, ForeignKey("passageiros.id_passageiro"))
    motorista = relationship("Motorista", back_populates="viagem")
    veiculo = relationship("Veiculo", back_populates="viagem")
    passageiro = relationship("Passageiro", back_populates="viagem")


class Passageiro(Base):
    __tablename__ = "passageiros"
    id_passageiro = Column(Integer, primary_key=True)
    passageiro_nome = Column(String(90))
    passageiro_nota = Column(DECIMAL)
    passageiro_fone = Column(String(15))
    viagem = relationship("Viagem", back_populates="passageiro")


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-9-BANCO-DE-DADOS/AULA-10-SQLAlCHEMY/ATIVIDADE/Q03/env_q03/db_locadora.db",
        echo=True,
    )

    # Criar as tabelas no banco de dados
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # Populando a tabela "cores"
        preto = Cor(nome_cor="Preto")
        branco = Cor(nome_cor="Branco")
        prata = Cor(nome_cor="Prata")
        vermelho = Cor(nome_cor="Vermelho")
        azul = Cor(nome_cor="Azul")
        session.add_all([preto, branco, prata, vermelho, azul])
        session.commit()

        # Populando a tabela "veiculos"
        carro_sedan = Veiculo(
            veiculo_descricao="Carro Sedan",
            veiculo_placa="ABC1234",
            cor=preto,
        )
        suv = Veiculo(
            veiculo_descricao="SUV",
            veiculo_placa="XYZ5678",
            cor=branco,
        )
        caminhonete = Veiculo(
            veiculo_descricao="Caminhonete",
            veiculo_placa="DEF9876",
            cor=prata,
        )
        caminhao = Veiculo(
            veiculo_descricao="Caminhão",
            veiculo_placa="GHI6543",
            cor=vermelho,
        )
        van = Veiculo(
            veiculo_descricao="Van",
            veiculo_placa="JKL3210",
            cor=azul,
        )
        session.add_all([carro_sedan, suv, caminhonete, caminhao, van])
        session.commit()

        # Populando a tabela "motoristas"
        motorista1 = Motorista(
            nome_motorista="João da Silva",
            nota_motorista=4.5,
            veiculo=carro_sedan,
        )
        motorista2 = Motorista(
            nome_motorista="Maria Souza",
            nota_motorista=4.8,
            veiculo=suv,
        )
        motorista3 = Motorista(
            nome_motorista="José Santos",
            nota_motorista=4.2,
            veiculo=caminhonete,
        )
        motorista4 = Motorista(
            nome_motorista="Ana Oliveira",
            nota_motorista=4.6,
            veiculo=caminhao,
        )
        motorista5 = Motorista(
            nome_motorista="Carlos Pereira",
            nota_motorista=4.9,
            veiculo=van,
        )
        session.add_all([motorista1, motorista2, motorista3, motorista4, motorista5])
        session.commit()

        # Populando a tabela "passageiros"
        passageiro1 = Passageiro(
            passageiro_nome="Pedro",
            passageiro_nota=4.7,
            passageiro_fone="123456789",
        )
        passageiro2 = Passageiro(
            passageiro_nome="Mariana",
            passageiro_nota=4.3,
            passageiro_fone="987654321",
        )
        passageiro3 = Passageiro(
            passageiro_nome="Lucas",
            passageiro_nota=4.6,
            passageiro_fone="456789123",
        )
        passageiro4 = Passageiro(
            passageiro_nome="Juliana",
            passageiro_nota=4.8,
            passageiro_fone="789123456",
        )
        passageiro5 = Passageiro(
            passageiro_nome="Gabriel",
            passageiro_nota=4.4,
            passageiro_fone="321654987",
        )
        session.add_all(
            [passageiro1, passageiro2, passageiro3, passageiro4, passageiro5]
        )
        session.commit()

        # Populando a tabela "viagens"
        viagem1 = Viagem(
            viagem_origem="Cidade A",
            viagem_destino="Cidade B",
            viagem_partida=date(2024, 3, 15),
            viagem_chegada=date(2024, 3, 16),
            viagem_duracao=1,
            motorista=motorista1,
            veiculo=carro_sedan,
            passageiro=passageiro1,
        )
        viagem2 = Viagem(
            viagem_origem="Cidade B",
            viagem_destino="Cidade C",
            viagem_partida=date(2024, 3, 17),
            viagem_chegada=date(2024, 3, 18),
            viagem_duracao=1,
            motorista=motorista2,
            veiculo=van,
            passageiro=passageiro2,
        )
        viagem3 = Viagem(
            viagem_origem="Cidade C",
            viagem_destino="Cidade D",
            viagem_partida=date(2024, 3, 19),
            viagem_chegada=date(2024, 3, 20),
            viagem_duracao=1,
            motorista=motorista3,
            veiculo=suv,
            passageiro=passageiro3,
        )
        viagem4 = Viagem(
            viagem_origem="Cidade D",
            viagem_destino="Cidade E",
            viagem_partida=date(2024, 3, 21),
            viagem_chegada=date(2024, 3, 22),
            viagem_duracao=1,
            motorista=motorista4,
            veiculo=caminhonete,
            passageiro=passageiro4,
        )
        viagem5 = Viagem(
            viagem_origem="Cidade E",
            viagem_destino="Cidade F",
            viagem_partida=date(2024, 3, 23),
            viagem_chegada=date(2024, 3, 24),
            viagem_duracao=1,
            motorista=motorista5,
            veiculo=caminhao,
            passageiro=passageiro5,
        )
        session.add_all([viagem1, viagem2, viagem3, viagem4, viagem5])
        session.commit()
