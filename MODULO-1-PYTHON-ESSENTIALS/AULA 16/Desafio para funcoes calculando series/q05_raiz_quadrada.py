import math

erro = 0.00001

def minha_raiz_quadrada(x):
    r_zero = x
    r_anterior = r_zero
    r_calculado = r_zero + 2*erro

    while abs(r_calculado - r_anterior) > erro:
        r_anterior = r_calculado
        r_calculado = (r_anterior + x/r_anterior)/2
    return round(r_calculado)

x = 144
print("Biblioteca math")
print(f"Raiz quadrada de {x}: {math.sqrt(x)}")
print()
print("Minha função de raiz quadrada")
print(f"Raiz quadrada de {x}: {minha_raiz_quadrada(x)}")