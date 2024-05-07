from sqlalchemy.orm import Mapped, mapped_column, relationship
from infra.config.base import Base


class Produto(Base):
    __tablename__ = "produtos"

    codigo: Mapped[int] = mapped_column(primary_key=True)
    modelo: Mapped[str] = mapped_column(nullable=False)
    marca: Mapped[str] = mapped_column(nullable=False)
    preco_compra: Mapped[float] = mapped_column(nullable=False)
    preco_venda: Mapped[float] = mapped_column(nullable=False)
    venda = relationship("Venda", backref="venda", lazy="subquery")
    estoque = relationship("Estoque", backref="estoque", lazy="subquery")
