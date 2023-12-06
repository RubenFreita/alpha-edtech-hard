

def avaliar_candidato(valor, callback_true, callback_false):

    if valor > 0:
        callback_true()
    elif valor < 0:
        callback_false()

def callback_true():
    print("O valor é verdadeiro!")

def callback_false():
    print("O valor não é verdadeiro!")

avaliar_candidato(5, callback_true, callback_false)
avaliar_candidato(-1, callback_true, callback_false)