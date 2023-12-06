
#função pura
def soma(a, b):
    return a + b
#A função acima é pura porque ela sempre retornará o mesmo
#resultado se setada com os mesmo dados e também porque
#não altera variáveis globais



lista_nomes = ["ruben", "freitas"]


#função impura
def adiciona_nome(nome):
    global lista_nomes
    lista_nomes.append(nome)
#A função acima é impura porque altera uma lista global

print(soma(2,5))
adiciona_nome("vasconcelos")
print(lista_nomes)