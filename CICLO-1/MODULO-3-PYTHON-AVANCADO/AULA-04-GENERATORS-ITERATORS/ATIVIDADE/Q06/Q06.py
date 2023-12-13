

pares_lista = [x for x in range(1, 11) if x %2==0]

print(pares_lista)
#O list comprehension itera sobre todo o range de uma vez
#e guarda todos os valores pares dentro da lista pares_lista



pares_generator = (x for x in range(1, 11) if x %2==0)
print(pares_generator)
print(next(pares_generator))

#já o generator cria o objeto generator pares_generator
# e só itera sobre o range quando solicitado um novo elemento