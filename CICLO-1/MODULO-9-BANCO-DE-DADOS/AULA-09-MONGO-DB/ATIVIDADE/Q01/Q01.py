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


new_cliente = {
    "nome": "Daniel",
    "cpf": 12345678910,
    "email": "daniel@teste.com",
    "cidade": "Marco",
    "idade": 27,
}
clientes.insert_one(new_cliente)


for cliente in clientes.find():
    print(cliente)
