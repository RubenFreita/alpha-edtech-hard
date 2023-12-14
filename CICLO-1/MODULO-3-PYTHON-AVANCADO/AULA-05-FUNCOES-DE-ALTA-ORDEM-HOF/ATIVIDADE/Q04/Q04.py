 
lista_dicionario = [{ "valor": 1,  "nome": "melancia"},
                    { "valor": 2,  "nome": "morango"}, 
                    { "valor": 9,  "nome": "limao"},
                    { "valor": 10, "nome": "caju"}, 
                    { "valor": 4,  "nome": "acerola"}
                    ]

menor = min(lista_dicionario, key= lambda dicionario: dicionario["valor"])
print(menor)