from pymongo import MongoClient


def insere_documento(nome_cliente, nome_colecao, new_documento):

    try:
        cliente = MongoClient("mongodb://localhost:27017/")

        db = cliente[nome_cliente]

        colecao = db[nome_colecao]
        colecao.insert_one(new_documento)
    except Exception as e:
        print(e)


documento = {"nome": "Cassio", "idade": 15, "curso": "Contabilidade"}
insere_documento(
    nome_cliente="atividade_1",
    nome_colecao="alunos",
    new_documento=documento,
)
