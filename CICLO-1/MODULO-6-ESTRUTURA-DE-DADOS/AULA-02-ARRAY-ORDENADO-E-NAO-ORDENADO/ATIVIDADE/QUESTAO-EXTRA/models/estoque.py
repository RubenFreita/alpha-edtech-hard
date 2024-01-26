# import sys
# sys.path.append(r'C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-6-ESTRUTURA-DE-DADOS/AULA-02/ATIVIDADE/Q01')

from prettytable import PrettyTable

from .produto import Produto
from .lista_modificada import ListaModificada


class Estoque:
    def __init__(self) -> None:
        self.produtos = ListaModificada()

    def adicionar_produtos(self, produto: Produto, qtd: int) -> None:
        self.produtos.append({"produto": produto, "quantidade": qtd})
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
        # Aqui eu instancio a tabela
        tabela = PrettyTable()

        # Aqui eu defino os nomes das colunas
        tabela.field_names = ["Id", "Nome", "Preço", "Quantidade"]

        # e aqui ele vai preenchendo as linhas dentro do for
        for produto in self.produtos:
            tabela.add_row(
                [
                    produto["produto"].id,
                    produto["produto"].nome,
                    produto["produto"].valor,
                    produto["quantidade"],
                ]
            )

        print("\n============= Lista de Produtos ==============")
        print(tabela, end="\n\n")
        # for produto in self.produtos:
        #     p = "produto"
        #     q = "quantidade"
        #     print(f"Indice: {produto[p].id}, Nome: {produto[p].nome}, Quantidade: {produto[q]}, Valor: {produto[p].valor}")
        # print("====================================================\n")
