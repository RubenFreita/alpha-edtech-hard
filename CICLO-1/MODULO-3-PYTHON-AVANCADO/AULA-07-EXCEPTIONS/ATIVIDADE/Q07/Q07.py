

def divisao_sem_erro(dividendo, divisor):
    for i in range(len(dividendo)):
        try:
            resultado = dividendo[i]/divisor[i]
        except TypeError:
            print("Erro de Tipo!")
            print(f"O erro ocorreu no index {i}")
        except ZeroDivisionError:
            print("Erro de Divisão por Zero!")
            print(f"O erro ocorreu no index {i}")
        except:
            print("Outros erros identificados!")
            print(f"O erro ocorreu no index {i}")
        else:
            print(f"O resultado da divisão de {dividendo[i]}/{divisor[i]} é igual a {resultado} ")
        print("==============================================")


dividendo = [2, "s", "4", 7, 0]
divisor =   [1, 3, 1, 0, "10"]
divisao_sem_erro(dividendo, divisor)