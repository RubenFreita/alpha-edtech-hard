#Compreensão de Lista
lista_quadrados2 = []
for x in range(1, 6):
    lista_quadrados2.append(x**2)
print(lista_quadrados2)
print(type(lista_quadrados2))

# Compreensão de Lista
lista_quadrados = [x**2 for x in range(1, 6)]
print(lista_quadrados)
print(type(lista_quadrados))




generator_quadrados = (x**2 for x in range(1, 6))
print(generator_quadrados)
print(next(generator_quadrados))
print(next(generator_quadrados))
print(next(generator_quadrados))
print(next(generator_quadrados))
print(type(generator_quadrados))