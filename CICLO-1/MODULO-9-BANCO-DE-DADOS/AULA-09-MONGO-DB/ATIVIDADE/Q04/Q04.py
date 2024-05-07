import dotenv as dt
import os

from pymongo import MongoClient

# Carregar variáveis de ambiente
dt.load_dotenv()

# Utilizar as variáveis de ambiente
mongodb_uri = os.getenv("MONGODB_URI")
cliente = MongoClient(mongodb_uri)
meu_db = cliente["atividade_aula_9"]

colecao_produto = meu_db["produto"]
colecao_pedido = meu_db["pedido"]


try:
    # Iniciando uma sessão
    with cliente.start_session() as secao:
        with secao.start_transaction():
            # Executar operações dentro da transação
            documento_arroz = {"id": 1, "nome": "arroz", "valor": 4.32}
            documento_feijao = {"id": 2, "nome": "feijao", "valor": 9.32}
            colecao_produto.insert_many([documento_arroz, documento_feijao])

            # usando a denormalização para facilitar as consultas
            documento_pedido1 = {
                "codigo": 1,
                "itens": [
                    {"produto": "arroz", "quantidade": 3},
                    {"produto": "feijao", "quantidade": 5},
                ],
            }
            documento_pedido2 = {
                "codigo": 2,
                "itens": [
                    {"produto": "arroz", "quantidade": 2},
                    {"produto": "feijao", "quantidade": 10},
                ],
            }
            colecao_pedido.insert_many([documento_pedido1, documento_pedido2])

            # Criando um índice único no campo 'id'
            colecao_produto.create_index([("id", 1)], unique=True)
            # Criando um índice único no campo 'codigo'
            colecao_pedido.create_index([("codigo", 1)], unique=True)

            # criando um indice para facilitar a busca do produto pelo indice
            colecao_produto.create_index([("nome", 1)])

            print("\nProdutos")
            for i in colecao_pedido.find():
                print(i)
            print("\nPedidos")
            for i in colecao_produto.find():
                print(i)
except Exception as e:
    print(e)
