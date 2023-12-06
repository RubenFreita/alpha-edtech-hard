conjunto_dados = [(1, 3.45, "20231120"), (2, 4.45, "20231120"), 
                  (10, 10.25, "20231020"), (1, 1.25, "20231125"), 
                  (10, 5.75, "20231125"), (8, 9.45, "20231129"), ]
ids_unicos = set()
datas_unicas = set()
ids = []

for dados in conjunto_dados:
    ids_unicos.add(dados[0])
    datas_unicas.add(dados[2])
    ids.append(dados[0])

print(f"O conjunto das datas únicas é: {datas_unicas}")


