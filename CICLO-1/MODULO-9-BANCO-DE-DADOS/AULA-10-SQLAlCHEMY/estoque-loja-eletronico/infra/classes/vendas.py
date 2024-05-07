from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from infra.config.base import Base
from datetime import date


class Venda(Base):
    __tablename__ = "vendas"

    id: Mapped[int] = mapped_column(primary_key=True)
    codigo_produto: Mapped[int] = mapped_column(ForeignKey("produtos.codigo"))
    data_venda: Mapped[date] = mapped_column(nullable=False)
    marca: Mapped[str] = mapped_column(nullable=False)
    valor: Mapped[float] = mapped_column(nullable=False)
