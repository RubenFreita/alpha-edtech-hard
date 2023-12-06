conjunto_dados = [(1, 3.45, "13/04/2023"), (2, 4.45, "11/04/2023"), 
                  (10, 10.25, "05/04/2023"), (1, 1.25, "05/04/2023"), 
                  (10, 5.75, "17/04/2023"), (8, 9.45, "09/04/2023"), ]
ids_unicos = set()

for dados in conjunto_dados:
    ids_unicos.add(dados[0])

print("Os IDs únicos dos produtos vendidos são:")
print(ids_unicos)