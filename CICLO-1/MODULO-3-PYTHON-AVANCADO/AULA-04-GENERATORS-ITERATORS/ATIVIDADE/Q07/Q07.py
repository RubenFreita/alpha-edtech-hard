

generator = (i*2 for i in (x for x in range(1, 20) if x%2==0))
#Assim como o list comprehension o generator também faz ser possível 
#o aninhamento de mais de um generator.
#Neste exemplo estou usando um generator mais interno (x for x in range(1, 20) if x%2==0)
#que irá retornar todos os x que são par em seguida esse objeto generator será iterado pelo
#generator mais externo que irá multiplicar por 2 todos os valores de x calculados pelo
#generator mais interno.



for i in generator:
    print(i)