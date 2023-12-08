from typing import List

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


def processa_produtos(produtos: List[Produto]) -> float:
    for index, produto in enumerate(produtos):
        if type(produto) == str:
            produtos[index] = Produto(str(produto), 0.0)
    produtos = []
    
    total = sum(produto.preco for produto in produtos)
    return total


# Lista de produtos
lista_produtos: List[Produto] = [
    Produto("Camiseta", 25.99),
    Produto("Calça", 39.99),
    Produto("Sapato", 59.99),
    # "Bolsa" # Erro: inserindo um objeto não Produto na lista
]
#para resolver o problema de tipo neste exemplo eu tive que 
#fazer com que a lista de produtos fosse tipada para que só recebesse 
#objetos do tipo produto

resultado = processa_produtos(lista_produtos)
print(f"Total dos produtos: R${resultado}")
