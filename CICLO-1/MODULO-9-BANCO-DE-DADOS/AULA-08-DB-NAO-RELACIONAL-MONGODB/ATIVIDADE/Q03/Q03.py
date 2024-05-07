from pymongo import MongoClient


def atualiza_documento(nome_cliente, nome_colecao, **kwargs):

    try:
        cliente = MongoClient("mongodb://localhost:27017/")

        db = cliente[nome_cliente]
        chaves = list(kwargs.keys())
        valores = list(kwargs.values())
        colecao = db[nome_colecao]
        colecao.update_one({chaves[0]: valores[0]}, {"$set": {chaves[1]: valores[1]}})

    except Exception as e:
        print(e)


atualiza_documento(
    nome_cliente="atividade_1",
    nome_colecao="alunos",
    curso="Pedagogia",
    nome="Liliane",
)
