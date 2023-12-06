#Questão 05


def substituiVogais(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace("a","*")
    palavra = palavra.replace("e","*")
    palavra = palavra.replace("i","*")
    palavra = palavra.replace("o","*")
    palavra = palavra.replace("u","*")
    return palavra

palavra = input("Digite uma palavra: ")

print(substituiVogais(palavra))
