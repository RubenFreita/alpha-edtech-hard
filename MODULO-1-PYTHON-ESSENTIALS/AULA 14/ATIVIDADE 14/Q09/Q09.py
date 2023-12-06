# import modulo_calculadora as calc
import importlib

calc = importlib.import_module("modulo_calculadora")
a = 2
b = 4
while 1:
    print("Digite 0 para sair.")
    print("Digite 1 se deseja realizar a soma.")
    print("Digite 2 se deseja atualizar o modulo calculadora.")
    opcao = input("Informe uma opção: ")
    print()
    if opcao == "0":
        break
    elif opcao == "1":
        print(f"A soma resulta em: {calc.soma(a,b)}")
        print()
    elif opcao == "2":
        print("Atualizando modulo...")
        importlib.reload(calc)
        print()