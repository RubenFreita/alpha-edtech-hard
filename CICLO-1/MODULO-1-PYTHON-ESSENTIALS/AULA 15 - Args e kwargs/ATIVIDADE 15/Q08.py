

def teste_kargs(carro, velocidade, **valores):
    print(carro)
    print(velocidade)
    for i in valores.values():
        print(i)



print("teste 1")
teste_kargs("carro", 100, nome="jose", chave="teste")
print()
print("teste 2")
teste_kargs("carro", 100, nome="jose", chave="teste", outraChave="brasil", oo="python")