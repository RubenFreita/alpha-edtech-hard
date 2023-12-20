

def quadrado(numero):
    try:
        inteiro = int(numero)
    except:
        print("A entrada não é um número válido")
        return f"O quadrado de {numero} não pode ser calculado!"
    else:
        print("Calculando...")
        return f"O quadrado do {int(numero)} é {inteiro**2}"
    finally:
        print("Fim da execução do algoritmo!")


print(quadrado(4.3))
print("====================================")
print(quadrado("3"))
print("====================================")
print(quadrado("s"))
print("====================================")
print(quadrado(True))