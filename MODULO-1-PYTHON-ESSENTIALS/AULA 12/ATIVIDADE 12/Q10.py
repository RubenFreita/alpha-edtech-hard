
informacoes_pessoais = {"nome": "augusto",
                        "idade": 26,
                        "profissao": "dev",
                        "filme_favorito": "interestelar",
                        "familiares": {
                            "pai": "jose",
                            "mae": "maria",
                            "avo": "sebastiao"
                        }}
#capturando as chaves com o método keys()
lista_chaves = informacoes_pessoais.keys()
#capturando os valores com o método values()
lista_valores = informacoes_pessoais.values()

print("Chaves: ")
print(lista_chaves)
print("Valores: ")
print(lista_valores)