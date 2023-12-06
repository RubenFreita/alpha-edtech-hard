#Questão 09


with open("palavras.txt", "w") as arquivo:
    arquivo.write("Ola Mundo!!!!\n")
    arquivo.write("Ola Mundo!!!!")

#A leitura do arquivo é feita apenas para demonstrar que está tudo funcionando
with open("palavras.txt", "r") as arquivo:
    print(arquivo.read())