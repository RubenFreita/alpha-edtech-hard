
def atribui_um(numero):
    return numero + 1


def soma_um_em_todos(lista, funcao):
    return [funcao(i) for i in lista]

lista = [ 1,2,3,4,5,6,7,8,9]
print(f"Lista antes: {lista}")
print(f"Lista depois: {soma_um_em_todos(lista, atribui_um)}")
