from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    Session,
    declarative_base,
    mapped_column,
    Mapped,
)
from typing import Any, List


declarative_base


class Base(DeclarativeBase):
    pass


class Produto(Base):
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    peso: Mapped[float] = mapped_column(nullable=False)
    valor: Mapped[float]
    # item_pedido = relationship("ItemPedido", back_populates="produto")


class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    valor_pedido: Mapped[float] = mapped_column(server_default="0.0")
    itens_pedidos: Mapped[List["ItemPedido"]] = relationship(
        "ItemPedido",
        backref="pedido",
        cascade="all, delete-orphan",
        lazy="subquery",
    )

    def __init__(self, **kw: Any):
        super().__init__(**kw)


class ItemPedido(Base):
    __tablename__ = "item_pedidos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    valor_item: Mapped[float] = mapped_column(DECIMAL, server_default="0.0")
    qtd_produto: Mapped[int] = mapped_column(nullable=False)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"))
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"))
    produto = relationship("Produto", backref="produtos")


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-9-BANCO-DE-DADOS/AULA-10-SQLAlCHEMY/ATIVIDADE/Q01-Mapped/env_q01/db_mercantil.db",
        echo=True,
    )

    # Criar as tabelas no banco de dados
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        produto1 = Produto(id=1, nome="Produto1", peso=1.5, valor=10.99)
        produto2 = Produto(id=2, nome="Produto2", peso=2.0, valor=15.99)
        produto3 = Produto(id=3, nome="Produto3", peso=1.8, valor=12.49)
        produto4 = Produto(id=4, nome="Produto4", peso=2.2, valor=19.99)
        produto5 = Produto(id=5, nome="Produto5", peso=2.5, valor=24.99)

        # item_pedido1 = ItemPedido(id=1, produto=produto1, qtd_produto=3)
        pedido1 = Pedido(
            id=1,
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(id=1, qtd_produto=3),
                ItemPedido(id=2, produto=produto2, qtd_produto=2),
            ],
        )
        pedido2 = Pedido(
            id=2,
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(id=3, produto=produto3, qtd_produto=1),
                ItemPedido(id=4, produto=produto4, qtd_produto=2),
            ],
        )
        pedido3 = Pedido(
            id=3,
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(id=5, produto=produto5, qtd_produto=3),
                ItemPedido(id=6, produto=produto1, qtd_produto=5),
            ],
        )
        pedido4 = Pedido(
            id=4,
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(id=7, produto=produto4, qtd_produto=3),
                ItemPedido(id=8, produto=produto5, qtd_produto=3),
            ],
        )
        pedido5 = Pedido(
            id=5,
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(id=9, produto=produto5, qtd_produto=1),
                ItemPedido(id=10, produto=produto2, qtd_produto=2),
            ],
        )

        session.add_all([pedido1, pedido2, pedido3, pedido4, pedido5])

        session.commit()
        data = (
            session.query(ItemPedido)
            .join(Produto)
            .with_entities(
                ItemPedido.id, ItemPedido.produto_id, ItemPedido.pedido_id, Produto.nome
            )
            .filter(ItemPedido.produto_id == Produto.id)
            .all()
        )

        for i in data:
            print(i)
