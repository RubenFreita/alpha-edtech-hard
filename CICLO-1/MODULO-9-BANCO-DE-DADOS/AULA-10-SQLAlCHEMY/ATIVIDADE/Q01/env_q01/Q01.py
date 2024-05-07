from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import DeclarativeBase, relationship, Session, declarative_base


declarative_base


class Base(DeclarativeBase):
    pass


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
    peso = Column(DECIMAL)
    valor = Column(DECIMAL)
    item_pedido = relationship("ItemPedido", back_populates="produto")


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    valor_pedido = Column(DECIMAL, server_default="0.0")
    itens_pedidos = relationship(
        "ItemPedido",
        back_populates="pedido",  # cascade="all, delete-orphan"
    )


class ItemPedido(Base):
    __tablename__ = "item_pedidos"

    id = Column(Integer, primary_key=True)
    valor_item = Column(DECIMAL, server_default="0.0")
    qtd_produto = Column(DECIMAL)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    produto = relationship("Produto", back_populates="item_pedido")
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    pedido = relationship("Pedido", back_populates="itens_pedidos")


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-9-BANCO-DE-DADOS/AULA-10-SQLAlCHEMY/ATIVIDADE/Q01/env_q01/db_mercantil.db",
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

        pedido1 = Pedido(
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(produto=produto1, qtd_produto=3),
                ItemPedido(produto=produto2, qtd_produto=2),
            ],
        )
        pedido2 = Pedido(
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(produto=produto3, qtd_produto=1),
                ItemPedido(produto=produto4, qtd_produto=2),
            ],
        )
        pedido3 = Pedido(
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(produto=produto5, qtd_produto=3),
                ItemPedido(produto=produto1, qtd_produto=5),
            ],
        )
        pedido4 = Pedido(
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(produto=produto4, qtd_produto=3),
                ItemPedido(produto=produto5, qtd_produto=3),
            ],
        )
        pedido5 = Pedido(
            valor_pedido=0,
            itens_pedidos=[
                ItemPedido(produto=produto5, qtd_produto=1),
                ItemPedido(produto=produto2, qtd_produto=2),
            ],
        )

        session.add_all([pedido1, pedido2, pedido3, pedido4, pedido5])

        session.commit()
