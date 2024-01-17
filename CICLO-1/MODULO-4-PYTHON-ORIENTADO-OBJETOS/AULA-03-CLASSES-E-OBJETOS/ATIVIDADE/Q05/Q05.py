
class Produto:
    id = 0
    #dicionário compartilhado que contém todos os produtos que
    #será instânciados
    produtos_cadastrados = dict()
    def __init__(self, nome: str, peso: str, valor: float) -> None:
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.clientes = set()
        self.id = Produto.id
        Produto.produtos_cadastrados[self.id] = self
        Produto.id += 1
    
    def __str__(self):
        return self.nome


class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    def __str__(self):
        return self.nome


class Pedido:

    def __init__(self, codigo: int, cliente: Cliente) -> None:
        self.codigo = codigo
        self.itens = []
        self.valor_pedido = 0
        self.cliente = cliente

        
    def adicionar_produto(self, novo_produto: Produto, qtd_produto: int):
        adiciona_novo_produto = True
        for item in range(len(self.itens)):
            if novo_produto.nome == self.itens[item][0]:
                qtd_total_produto = qtd_produto + self.itens[item][1]
                self.itens[item] = (novo_produto.nome, qtd_total_produto)
                adiciona_novo_produto = False
                break
        if adiciona_novo_produto:
            self.itens.append((novo_produto.nome, qtd_produto))
            novo_produto.clientes.add(self.cliente.nome)
        self.valor_pedido += round(qtd_produto * novo_produto.valor, 2)
        
        

if __name__ == "__main__":
    
    arroz = Produto("Arroz", "1 Kg", 6.50)
    feijao = Produto("Feijão", "1 Kg", 8.30)
    macarrao = Produto("Macarrão", "500 gramas", 4.50)
    farinha_trigo = Produto("Farinha de trigo", "1 Kg", 10.50)
    frango = Produto("Frango", "1 Kg", 14.50)

    cliente1 = Cliente("Ruben")
    cliente2 = Cliente("João")
    cliente3 = Cliente("Maria")

    pedido1 = Pedido(12345, cliente1)
    pedido1.adicionar_produto(arroz, 2)
    pedido1.adicionar_produto(arroz, 2)
    pedido1.adicionar_produto(feijao, 4)
    pedido1.adicionar_produto(macarrao, 2)
    pedido1.adicionar_produto(feijao, 1)
    pedido1.adicionar_produto(frango, 1)

    pedido2 = Pedido(23415, cliente2)
    pedido2.adicionar_produto(feijao, 4)
    pedido2.adicionar_produto(frango, 2)
    pedido2.adicionar_produto(macarrao, 1)
    pedido2.adicionar_produto(farinha_trigo, 1)

    pedido3 = Pedido(23875, cliente3)
    pedido3.adicionar_produto(frango, 2)
    pedido3.adicionar_produto(arroz, 5)

    pedido4 = Pedido(15635, cliente1)
    pedido4.adicionar_produto(farinha_trigo, 2)
    pedido4.adicionar_produto(macarrao, 1)
    pedido4.adicionar_produto(feijao, 2)

    print(f"Lista de itens do Pedido {pedido1.codigo}, itens: {pedido1.itens}")
    print(f"Valor do pedido {pedido1.codigo}: R$ {pedido1.valor_pedido}")
    print(f"Cliente: {pedido1.cliente.nome}")
    print()
    print(f"Lista de itens do Pedido {pedido2.codigo}, itens: {pedido2.itens}")
    print(f"Valor do pedido {pedido2.codigo}: R$ {pedido2.valor_pedido}")
    print(f"Cliente: {pedido2.cliente.nome}")
    print()
    print(f"Lista de itens do Pedido {pedido3.codigo}, itens: {pedido3.itens}")
    print(f"Valor do pedido {pedido3.codigo}: R$ {pedido3.valor_pedido}")
    print(f"Cliente: {pedido3.cliente.nome}")
    print()
    print(f"Lista de itens do Pedido {pedido4.codigo}, itens: {pedido4.itens}")
    print(f"Valor do pedido {pedido4.codigo}: R$ {pedido4.valor_pedido}")
    print(f"Cliente: {pedido4.cliente.nome}")

    print()
    print(f"Clientes que compraram Arroz: {arroz.clientes}")
    print(f"Clientes que compraram Feijão: {feijao.clientes}")
    print(f"Clientes que compraram Macarrão: {macarrao.clientes}")
    print(f"Clientes que compraram Farinha de Trigo: {farinha_trigo.clientes}")
    print(f"Clientes que compraram Frango: {frango.clientes}")
    print()

#mostrando o dicionário de produtos instânciados.
    print("Produtos:")
    for i, produto in arroz.produtos_cadastrados.items():
        print(f"{i}: {produto}")
    print(arroz.produtos_cadastrados)