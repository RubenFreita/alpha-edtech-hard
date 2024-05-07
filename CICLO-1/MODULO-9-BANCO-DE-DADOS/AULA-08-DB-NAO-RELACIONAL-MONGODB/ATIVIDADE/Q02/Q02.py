from pymongo import MongoClient


def mostra_documentos(nome_cliente, nome_colecao):

    try:
        cliente = MongoClient("mongodb://localhost:27017/")

        db = cliente[nome_cliente]

        colecao = db[nome_colecao]
        documentos = colecao.find()
        keys = list(documentos[0].keys())
        print(f"{keys[1]}\t{keys[2]}")
        for documento in documentos:

            print(f"{documento['nome']}\t {documento['idade']}")
    except Exception as e:
        print(e)


mostra_documentos(
    nome_cliente="atividade_1",
    nome_colecao="alunos",
)
