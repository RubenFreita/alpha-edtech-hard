



def executar_operacao(numero, operacao):
    return operacao(numero)

# Callback para calcular o quadrado
def quadrado(num):
    return num ** 2

# Callback para calcular o inverso
def inverso(num):
    if num != 0:
        return round(1 / num , 2)
    else:
        return "Divisão por zero não permitida"
    
numero = 6
numero1 = 0
print(f"Quadrado de {numero}:", executar_operacao(numero, quadrado))
print(f"Inverso de {numero}:", executar_operacao(numero, inverso))
print(f"Inverso de {numero1}:", executar_operacao(numero1, inverso))