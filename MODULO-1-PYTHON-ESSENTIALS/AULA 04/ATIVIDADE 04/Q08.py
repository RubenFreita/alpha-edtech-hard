#Questão 08

litros = float(input("Informe a quantidade de litros de combustível vendido: "))
print("Digite G para Gasolina e A para Álcool.")
tipoCombustivel = input("Informe o tipo de Combustível: ")
valorAPagar = 0
if litros <=20:
    if tipoCombustivel.lower() == "g":
        valorAPagar = litros*2.5
        valorAPagar = valorAPagar - valorAPagar*0.04
    elif tipoCombustivel.lower() == "a":
        valorAPagar = litros*1.9
        valorAPagar = valorAPagar - valorAPagar*0.03
elif litros > 20:
    if tipoCombustivel.lower() == "g":
        valorAPagar = litros*2.5
        valorAPagar = valorAPagar - valorAPagar*0.06
    if tipoCombustivel.lower() == "a":
        valorAPagar = litros*1.9
        valorAPagar = valorAPagar - valorAPagar*0.05

print(f"O valor total a pagar será de R$ {valorAPagar:.2f}")