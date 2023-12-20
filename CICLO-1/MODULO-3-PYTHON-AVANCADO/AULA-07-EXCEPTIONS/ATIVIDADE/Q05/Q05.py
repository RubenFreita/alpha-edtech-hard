from typing import Union, List

lista = [ 1,2,3,4,5]


def retorna_elemento(index: int, lista: List[int]) -> Union[None, int]:
    try:
        elemento = lista[int(index)]
    except IndexError:
        print("Index informado fora do limites de range da lista!")
    else:
        print("Index informado dentro do limite de rante da lista!")
        return elemento
    
def leitura_arquivo(nome_arquivo: str):
    try:
        try:
            with open(nome_arquivo, "r") as arquivo:
                leitura = arquivo.read()
            
        except FileNotFoundError:
            print(f"O arquivo \"{nome_arquivo}\" não existe!")
            return "Leitura indisponível"
        except PermissionError:
            print(f"Você não tem permissão para ler este arquivo!")
            return "Leitura indisponível"
        else:
            return leitura
    except Exception as e:
        print('Outras exceções de leitura do arquivo!')
        print(e)
        return "Problema na leitura do arquivo!"
    
print("============TESTES DE RETORNO DE VALOR DA LISTA===========")
valor1 = retorna_elemento(2,lista)
print(f"Valor da primeira chamada: {valor1}")
valor2 = retorna_elemento(10, lista)
print(f"Valor da segunda chamada: {valor2}")
print()

print("============TESTES LEITURA DE ARQUIVO===========")

#arquivo foi criado e retirado todas as permissões para dar erro de permissão
leitura1 = leitura_arquivo("teste.txt")
print(leitura1)
leitura2 = leitura_arquivo("test.txt")
print(leitura2)