
def informacoes_animais(informacao):

    if isinstance(informacao, str):
        return f"O som do animal é: {informacao.capitalize()}!"
    elif isinstance(informacao, int):
        return f"O animal tem {informacao} anos de idade."
    elif isinstance(informacao, list):
        return f"Há {len(informacao)} animais na lista."
    else:
        return "Tipo de informação não suportado.".upper()

# Chamada da função com diferentes tipos de dados
resultado_1 = informacoes_animais("miau")
resultado_2 = informacoes_animais(3)
resultado_3 = informacoes_animais(["gato", "cachorro", "pássaro"])
resultado_4 = informacoes_animais((1,2))

print(resultado_1)
print(resultado_2)
print(resultado_3)
print(resultado_4)
