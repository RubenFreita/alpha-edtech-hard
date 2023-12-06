#Questão 06

print("Informe dois número e escolha a operação que deseja realizar.")
entrada1 = float(input("Digite o primeiro número: "))
entrada2 = float(input("Digite o segundo número: "))

print("Escolha um número de 1 a 3 de acordo com\n a operação que deseja realizar:")
print("1 - Par ou Ímpar")
print("2 - Inteiro ou Decimal")
print("3 - Positivo ou Negatico")
opcao = int(input("informa a opção desejada: "))

if opcao == 1:
    if entrada1 % 2 ==0:
        print(f"O número {entrada1} é par")
    else:
        print(f"O número {entrada1} é ímpar")
    if entrada2 % 2 ==0:
        print(f"O número {entrada2} é par")
    else:
        print(f"O número {entrada2} é ímpar")
elif opcao == 2:
    if entrada1 % 1 == 0:
        print(f"O número {entrada1} é inteiro")
    else:
        print(f"O número {entrada1} é decimal")
    if entrada2 % 1 == 0:
        print(f"O número {entrada2} é inteiro")
    else:
        print(f"O número {entrada2} é decimal")
elif opcao == 3:
    if entrada1 < 0:
        print(f"O número {entrada1} é negativo")
    else:
        print(f"O número {entrada1} é positivo")
    if entrada2 < 0:
        print(f"O número {entrada2} é negativo")
    else:
        print(f"O número {entrada2} é positivo")
else:
    print("Opção escolhida inválida!")