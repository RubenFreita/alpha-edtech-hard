from typing import Union
def divisao_de_dois_numeros() -> None:

    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        print(f"A divisão de {x} por {y} é igual a: {x/y}")
    except ZeroDivisionError:
        print("Não foi possível realizar a divisão, porque o y é igual a zero.")
    except:
        print("Não foi possível realizar a divisão.")
    finally:
        print("Fim da execução do programa!")

divisao_de_dois_numeros()