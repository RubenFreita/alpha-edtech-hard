
informacoes_pessoais = {"nome": "augusto",
                        "idade": 26,
                        "profissao": "dev",
                        "filme_favorito": "interestelar",}

#verificação com chave existente no dicionario
nome_get = informacoes_pessoais.get("nome") # retorna o valor se ela existir no dicioná
nome_in = "nome" in informacoes_pessoais # retorna o True se ela existir no dicioná
print(nome_get)
print(nome_in)

#verificação sem chave existente no dicionario
altura_get = informacoes_pessoais.get("altura") #retorna None se não existir no dicionário
#retorna a frase padrãose não existir no dicionário
altura_get = informacoes_pessoais.get("altura", "A altura não existe neste dicionário!!") 
altura_in = "altura" in informacoes_pessoais # retorna o True se ela existir no dicioná
print(altura_get)
print(altura_in)
