from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from infra.config.base import Base
from datetime import date


class Estoque(Base):
    __tablename__ = "estoques"

    id: Mapped[int] = mapped_column(primary_key=True)
    produto_codigo: Mapped[int] = mapped_column(ForeignKey("produtos.codigo"))
    data_ultima_entrada: Mapped[date] = mapped_column(nullable=False)
    produtos_disponiveis: Mapped[str] = mapped_column(nullable=False)
    tipo: Mapped[str] = mapped_column(nullable=False)
    popular: Mapped[bool] = mapped_column(nullable=False)
