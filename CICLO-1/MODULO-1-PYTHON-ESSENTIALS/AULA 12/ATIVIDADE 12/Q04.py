
informacoes_pessoais = {"nome": "augusto",
                        "idade": 26,
                        "profissao": "dev",
                        "filme_favorito": "interestelar",}

#for percorrendo o dicionario e capturando a chave e valor de cada item
for chave, valor in informacoes_pessoais.items():
    print(f"chave: {chave}, valor: {valor}")