
class Produto():
    id = 0
    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome
        self.valor = valor
        self.id = Produto.id
        Produto.id += 1

    def __str__(self) -> str:
        return self.nome
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Produto) and self.nome == __value.nome:
            return True
        else:
            return False
    
    

class Estoque():
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produtos(self, produto: Produto, qtd: int) -> None:
        self.produtos.append({"produto":produto, "quantidade":qtd})
        print(f"Produto {produto.nome} adicionado com sucesso!")

    def atualizar_qtd_produto(self, produto, nova_qtd) -> None:
        flag = False
        for i, p in enumerate(self.produtos):
            if p["produto"] == produto:
                produto.id = p["produto"].id
                produto.valor = p["produto"].valor
                flag = True
                self.produtos[i] = {"produto": produto, "quantidade": nova_qtd}
                print(f"Produdo {produto.nome} atualizado com sucesso!")
        if flag == False:
            p = "produto"
            print(f"O Produdo {produto.nome} não foi encontrado na lista de produtos.")
            print("Tente adicionar o produto na lista de produtos!")

    def remover_produtos(self, produto) -> None:
        flag = False
        for i, p in enumerate(self.produtos):
            if p["produto"] == produto:
                flag = True
                self.produtos.pop(i)
                print(f"Produdo {produto.nome} removido com sucesso!")
        if flag == False:
            print(f"O Produdo {produto.nome} não foi encontrado na lista de produtos.")
            print("Portando não foi possível removê-lo.")

    def listar_produtos(self) -> None:
        print("\n=================Lista de Produtos==================")
        for produto in self.produtos:
            p = "produto"
            q = "quantidade"
            print(f"Indice: {produto[p].id}, Nome: {produto[p].nome}, Quantidade: {produto[q]}, Valor: {produto[p].valor}")
        print("====================================================\n")
    
def exibir_menu():
    print("\n===== Menu =====")
    print("1. Adicionar Produto")
    print("2. Atualizar Quantidade do Produto")
    print("3. Remover Produto")
    print("4. Listar Produtos")
    print("5. Sair")


def programa(estoque):
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            nome_produto = input("Digite o nome do produto: ")
            valor_produto = float(input("Digite o valor do produto: "))
            quantidade_produto = int(input("Digite a quantidade do produto: "))
            novo_produto = Produto(nome_produto, valor_produto)
            estoque.adicionar_produtos(novo_produto, quantidade_produto)

        elif opcao == "2":
            nome_produto = input("Digite o nome do produto a ser atualizado: ")
            quantidade_produto = int(input("Digite a nova quantidade: "))
            produto_a_atualizar = Produto(nome_produto, 0)
            estoque.atualizar_qtd_produto(produto_a_atualizar, quantidade_produto)

        elif opcao == "3":
            nome_produto = input("Digite o nome do produto a ser removido: ")
            produto_a_remover = Produto(nome_produto, 0)
            estoque.remover_produtos(produto_a_remover)

        elif opcao == "4":
            estoque.listar_produtos()

        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":

    estoque = Estoque()

    programa(estoque)
  