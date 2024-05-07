import dotenv as dt
import os

from pymongo import MongoClient

# Carregar variáveis de ambiente
dt.load_dotenv()

# Utilizar as variáveis de ambiente
mongodb_uri = os.getenv("MONGODB_URI")
cliente = MongoClient(mongodb_uri)
meu_db = cliente["atividade_aula_9"]

colecao = meu_db["cliente"]

# Iniciando uma sessão
with cliente.start_session() as secao:
    with secao.start_transaction():
        # Executar operações dentro da transação
        colecao.update_one({"nome": "Daniel"}, {"$set": {"cpf": 98765432100}})
        for i in colecao.find():
            print(i)
