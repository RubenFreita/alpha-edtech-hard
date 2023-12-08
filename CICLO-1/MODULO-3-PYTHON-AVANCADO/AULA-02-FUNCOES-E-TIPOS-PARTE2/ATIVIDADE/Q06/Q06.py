
def processa_informacao(informacao):

    if isinstance(informacao, str):
        return f"O som do animal é: {informacao.capitalize()}!"
    elif isinstance(informacao, int):
        return f"O animal tem {informacao} anos de idade."
    elif isinstance(informacao, list):
        return f"Há {len(informacao)} animais na lista."
    else:
        return "Tipo de informação não suportado."

# Chamada da função com diferentes tipos de dados
resultado_1 = processa_informacao("miau")
resultado_2 = processa_informacao(3)
resultado_3 = processa_informacao(["gato", "cachorro", "pássaro"])

print(resultado_1)
print(resultado_2)
print(resultado_3)
