import dotenv as dt
import os

from pymongo import MongoClient

# Carregar variáveis de ambiente
dt.load_dotenv()

# Utilizar as variáveis de ambiente
mongodb_uri = os.getenv("MONGODB_URI")
cliente = MongoClient(mongodb_uri)
meu_db = cliente["rede_social"]

usuario1 = {
    "nome": "Daniel",
    "cpf": 90345678910,
    "email": "daniel@teste.com",
    "cidade": "Marco",
    "idade": 27,
}

usuario2 = {
    "nome": "Matheus",
    "cpf": 1230988778910,
    "email": "matheus@teste.com",
    "cidade": "Amontada",
    "idade": 21,
}

usuario3 = {
    "nome": "Carlos",
    "cpf": 123456643910,
    "email": "carlos@teste.com",
    "cidade": "Fortaleza",
    "idade": 50,
}
usuario4 = {
    "nome": "Ruben",
    "cpf": 12345678910,
    "email": "ruben@teste.com",
    "cidade": "Marco",
    "idade": 24,
}
usuario5 = {
    "nome": "Ruben",
    "cpf": 90876734312,
    "email": "ruben.freitas@teste.com",
    "cidade": "Marco",
    "idade": 50,
}


# Iniciando uma sessão
with cliente.start_session() as secao:
    with secao.start_transaction():
        try:
            meu_db.colecao_usuarios.insert_many(
                [
                    usuario1,
                    usuario2,
                    usuario3,
                    usuario4,
                    usuario5,
                ]
            )

            meu_db.colecao_usuarios.create_index([("cpf", 1)], unique=True)
            meu_db.colecao_usuarios.create_index([("email", 1)], unique=True)
            meu_db.colecao_usuarios.create_index([("idade", 1), ("nome", 1)])
            for i in meu_db.colecao_usuarios.find(
                {"idade": {"$lt": 55}, "nome": "Ruben"}
            ):
                print(i)

        except Exception as e:
            secao.abort_transaction()
            print(f"Rollback realizado devido ao erro: {e}")
