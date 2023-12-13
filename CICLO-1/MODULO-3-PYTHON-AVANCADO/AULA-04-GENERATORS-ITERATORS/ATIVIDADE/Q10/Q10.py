

def convert_float_generator(l):
    i=0
    while i< len(l):
        try:
            yield float(l[i])
        except:
            yield 0.0
        i += 1

lista = ["2.4", "1", "oi", "3.6", "3,1"]

generator_float = convert_float_generator(lista)

for i in generator_float:
    print(i)

"""
Podemos ver que esse uso do generator ocasionará uma excessão de ValueError
que será capiturada e então dentro da except é retornado 0.0 usando o yield 
fazendo com que o fluxo do generator prossiga normalmente após capiturar a execessão.
"""
