from typing import Any
from infra.config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

    def __init__(self, nome, email, id=None, **kw: Any):
        super().__init__(**kw)
        self.id = id
        self.nome = nome
        self.email = email


class UsuarioGrupo(Base):
    __tablename__ = "usuarios_grupos"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    id_grupo: Mapped[int] = mapped_column(ForeignKey("grupos.id"))

    # def __init__(self, **kw: Any):
    #     super().__init__(**kw)


class Grupo(Base):
    __tablename__ = "grupos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome_grupo: Mapped[str] = mapped_column(nullable=False)


class Reacao(Base):
    __tablename__ = "reacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    reacao: Mapped[str] = mapped_column(nullable=False)
    id_mensagem: Mapped[int] = mapped_column(ForeignKey("mensagens.id"))


class Mensagem(Base):
    __tablename__ = "mensagens"

    id: Mapped[int] = mapped_column(primary_key=True)
    conteudo: Mapped[str] = mapped_column(nullable=False)
    id_usuario_grupo: Mapped[int] = mapped_column(ForeignKey("usuarios_grupos.id"))

    def __init__(self, id, conteudo, id_usuario_grupo, **kw: Any):
        super().__init__(**kw)
        self.id = id
        self.conteudo = conteudo
        self.id_usuario_grupo = id_usuario_grupo


class Resposta(Base):
    __tablename__ = "repostas"

    id: Mapped[int] = mapped_column(primary_key=True)
    conteudo: Mapped[str] = mapped_column(nullable=False)
    id_mensagem_respondida: Mapped[int] = mapped_column(ForeignKey("mensagens.id"))

    def __init__(self, id, conteudo, id_mensagem_respondida, **kw: Any):
        self.id = id
        self.conteudo = conteudo
        self.id_mensagem_respondida = id_mensagem_respondida
