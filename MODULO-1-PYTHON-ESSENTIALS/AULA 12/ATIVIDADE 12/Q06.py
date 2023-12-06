
informacoes_pessoais = {"nome": "augusto",
                        "idade": 26,
                        "profissao": "dev",
                        "filme_favorito": "interestelar",
                        "familiares": {
                            "pai": "jose",
                            "mae": "maria",
                            "avo": "sebastiao"
                            },
                        }
#remove o item informado no paramentro
remove_item = informacoes_pessoais.pop("familiares")
print(remove_item)
#remove o ultimo intem do dicionario
remove_item = informacoes_pessoais.popitem()
print(remove_item)

#removendo item com o delete
del informacoes_pessoais["idade"]
print()
print("print após remoções: ")
print(informacoes_pessoais)