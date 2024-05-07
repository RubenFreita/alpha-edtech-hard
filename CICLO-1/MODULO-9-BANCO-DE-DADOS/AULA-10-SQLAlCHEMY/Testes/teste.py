from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Criação do engine e da sessão
engine = create_engine("sqlite:///./testes/example.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Criação do banco de dados
Base = declarative_base()


# Definição das classes Usuario e Endereco
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = relationship("Endereco", back_populates="usuario")


class Endereco(Base):
    __tablename__ = "enderecos"
    id = Column(Integer, primary_key=True)
    rua = Column(String)
    cidade = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="endereco")

    def __init__(self, rua, cidade, usuario):
        if usuario is None:
            raise ValueError("Endereco must have an associated Usuario.")
        self.rua = rua
        self.cidade = cidade
        self.usuario = usuario


# Criação das tabelas
Base.metadata.create_all(engine)

# Inserção de dados
usuario1 = Usuario(nome="Mateus")
usuario2 = Usuario(nome="Jorge")

# Tentativa de criar um endereço sem usuário (vai gerar um erro)
try:
    endereco1 = Endereco(rua="Rua B", cidade="Cidade X", usuario=None)
except ValueError as e:
    print("Error:", e)

# Criar um endereço associado a um usuário existente
endereco1 = Endereco(rua="Rua A", cidade="Cidade X", usuario=[usuario1, usuario2])

# Adicionando os objetos ao banco de dados
session.add_all([usuario1, endereco1])

# Commit das transações
session.commit()

# Consulta para verificar se os dados foram inseridos corretamente
consulta_usuario = session.query(Usuario).first()
consulta_endereco = session.query(Endereco).first()

print("Usuário:", consulta_usuario.nome)
print("Endereço:", consulta_endereco.rua, "-", consulta_endereco.cidade)
