#Questão 09

qtdMorango = float(input("Informe a quantidade (em Kg) de Morango comprada: "))
qtdMaca = float(input("Informe a quantidade (em Kg) de Maçã comprada: "))
valorMorango = 0
valorMaca = 0
if 1 <= qtdMorango <= 5:
    valorMorango = qtdMorango*2.5
elif qtdMorango > 5:
    valorMorango = qtdMorango*2.2
if 1 <= qtdMaca <= 5:
    valorMaca = qtdMaca*1.8
elif qtdMaca > 5:
    valorMaca = qtdMaca*1.5
pesoTotal = qtdMaca+qtdMorango
valorTotal = valorMaca+valorMorango
if pesoTotal>8 or valorTotal>25:
    valorTotal = valorTotal - valorTotal*0.1

print(f"O valor a ser pago pelo cliente será de R$ {valorTotal:.2f}")