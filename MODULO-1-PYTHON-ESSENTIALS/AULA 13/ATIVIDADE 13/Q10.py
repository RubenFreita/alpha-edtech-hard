

def celsius_para_fahrenheit(temp):
    temp_fahrenheit = temp*1.8 + 32 
    return temp_fahrenheit

def fahrenheit_para_celsius(temp):
    temp_celsius = (temp - 32)*5/9
    return temp_celsius

def menu_escolha():
    print("=====BEM VINDO À CALCULADORA DE TEMPERATURA=====")
    while 1:
        print("Escolha uma das opções abaixo:")
        print("0 - Para Sair")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        opcao = input()
        if opcao == "0":
            print("Saindo da calculadora de Temperatura...")
            break
        elif opcao == "1":
            temp = float(input("Informe a temperatura em graus Celsius: "))
            celsius_para_fahrenheit(temp)
            print(f"A temperatura {temp}°C é igual a {celsius_para_fahrenheit(temp):.2f}°F")
            print()
        elif opcao == "2":
            temp = float(input("Informe a temperatura em graus Fahrenheit: "))
            fahrenheit_para_celsius(temp)
            print(f"A temperatura {temp}°F é igual a {fahrenheit_para_celsius(temp):.2f}°C")
            print()

menu_escolha()