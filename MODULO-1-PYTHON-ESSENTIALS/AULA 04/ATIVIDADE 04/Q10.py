#Questão 10

print("Seja Bem vindo ao Supermercado Tabajara!")
print("Escolha uma das opções de carne:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")
tipo = input("Digite a opção desejada: \n")
nomeTipoCarne = ""
qtdCarne = float(input("Informe a quantidade (em Kg) de carne comprada: \n"))
print("A compra será feita no cartão Tabajara ou outros?")
print("1 - Cartão Tabajara")
print("2 - Outros")
metodoPagamento = input("Informe o método de pagamento: ")
nomeMetodoPagamento = ""
valorCompra = 0
if 1 <= qtdCarne <= 5:
    if tipo == "1":
        nomeTipoCarne = "Filé Duplo"
        valorCompra = qtdCarne*5.8
    elif tipo == "2":
        nomeTipoCarne = "Alcatra"
        valorCompra = qtdCarne*6.8
    elif tipo == "3":
        nomeTipoCarne = "3 - Picanha"
        valorCompra = qtdCarne*7.8
    else:
        print("O programa será encerrado, pois foi informado uma opção inválida!")
        exit()
        
if qtdCarne > 5:
    if tipo == "1":
        valorCompra = qtdCarne*4.9
    elif tipo == "2":
        valorCompra = qtdCarne*5.9
    elif tipo == "3":
        valorCompra = qtdCarne*6.9
    else:
        print("O programa será encerrado, pois foi informado uma opção inválida!")
        exit()
valorTotalAPagar = 0
desconto = 0
if metodoPagamento == "1":
    nomeMetodoPagamento = "Cartão Tabajara"
    desconto = valorCompra*0.05
    valorTotalAPagar = valorCompra - desconto
else:
    valorTotalAPagar = valorCompra
    nomeMetodoPagamento = "Outros"

print(f"\t\t    Cupom Fiscal")
print(f"\t\tSupermercado Tabajara")
print(f"Tipo de Carne\t\t\t\t{nomeTipoCarne}")
print(f"Qtd de Carne\t\t\t\t{qtdCarne} Kg")
print(f"Preço Total\t\t\t\tR$ {valorCompra:.2f}")
print(f"Tipo de Pagamento\t\t\t{nomeMetodoPagamento}")
print(f"Valor do Desconto\t\t\tR$ {desconto:.2f}")
print("-------------------------------------------------------")
print(f"Valor a Pagar\t\t\t\tR$ {valorTotalAPagar:.2f}")

    

