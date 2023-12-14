from functools import reduce

lista_dicionario = [{ "valor": 1,  "nome": "melancia"},
                    { "familia": "freitas",  "regiao": "norte"}, 
                    { "anime": "one piece",  "filme": "vingadores"},
                    { "dia": 16, "produto": "mouse"}, 
                    { "carne": 4,  "fruta": "acerola"}
                    ]

def junta_dicionarios(dicionario1: dict, dicionario2: dict):
    for chave, valor in dicionario1.items():
        dicionario2[chave] = valor
    return dicionario2

dicionarios_juntos = reduce(junta_dicionarios, lista_dicionario)
print(dicionarios_juntos)
