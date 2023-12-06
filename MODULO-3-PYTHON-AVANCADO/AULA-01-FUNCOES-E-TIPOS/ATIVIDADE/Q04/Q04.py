

numero = 4

def altera_global(num):
    global numero
    numero += num

print("variavel global antes de alterar:")
print(numero)

altera_global(numero)
print("variavel global depois de alterar:")
print(numero)

altera_global(numero)
print("variavel global depois da segunda alteração:")
print(numero)

#podemos ver que passando a variavel global para alterar ela mesma via parametro
#de uma função irá modificar nas próximas vezes que a função altera for chamada]
#pois a variavel global terá um novo número na segunda chamada da função
#e a cada vez que se chamar a função o valor passado por parametro será diferente 