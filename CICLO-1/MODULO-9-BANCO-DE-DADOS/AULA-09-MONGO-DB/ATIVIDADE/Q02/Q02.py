import dotenv as dt
import os

from pymongo import MongoClient

# Carregar variáveis de ambiente
dt.load_dotenv()

# Utilizar as variáveis de ambiente
mongodb_uri = os.getenv("MONGODB_URI")
cliente = MongoClient(mongodb_uri)
meu_db = cliente["atividade_aula_9"]

clientes = meu_db["cliente"]

clientes.create_index(([("cidade", 1), ("idade", 1)]))

for i in clientes.find({"idade": {"$lt": 25}, "cidade": "Marco"}):
    print(i)
