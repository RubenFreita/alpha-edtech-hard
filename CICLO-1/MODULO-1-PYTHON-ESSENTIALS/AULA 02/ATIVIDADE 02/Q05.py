#Questão 05

nomeVendedor = input("Digite o nome do vendedor: ")
salarioVendedor = float(input("Digite o salário fixo do vendedor: "))
vendasDoMesVendedor = float(input("Digite o total de vendas realizadas pelo vendedor no mês(em dinheiro): "))

valorComissaoVendas = vendasDoMesVendedor * 0.05

totalAReceber = salarioVendedor + valorComissaoVendas

print(f"O valor total que o vendedor irá receber no final do mês é: R${totalAReceber:.2f}")
