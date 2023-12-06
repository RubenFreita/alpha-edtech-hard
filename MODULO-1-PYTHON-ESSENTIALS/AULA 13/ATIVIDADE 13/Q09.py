
#valida senha

def tam_valido(string):
    if len(string) < 8:
        return False
    return True
def contem_char(string):
    for i in str(string):
        if i.isalpha():
            return True
    return False
def contem_maiusculo(string):
    for i in str(string):
        if i.isupper():
            return True
    return False
def contem_minusculo(string):
    for i in str(string):
        if i.islower():
            return True
    return False
def contem_numero(string):
    for i in str(string):
        if i.isnumeric():
            return True
    return False
def contem_caractere_especial(string):
    caracteres_especiais = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"

    for char in string:
        if char in caracteres_especiais:
            return True
    return False

def verifica_validade(senha):
    if (tam_valido(senha) and contem_char(senha) and 
        contem_maiusculo(senha) and 
        contem_minusculo(senha) and 
        contem_caractere_especial(senha) and 
        contem_numero(senha)):
        return True
    return False


def imprime_validade(senha):
    if verifica_validade(senha):
        print(f"A senha \"{senha}\" é válida")
    else:
        print(f"A senha \"{senha}\" não é válida")

senha1 = "#100"
imprime_validade(senha1)
senha2 = "AlphaEdtech#100"
imprime_validade(senha2)
senha3 = "alphaedtech#100"
imprime_validade(senha3)

