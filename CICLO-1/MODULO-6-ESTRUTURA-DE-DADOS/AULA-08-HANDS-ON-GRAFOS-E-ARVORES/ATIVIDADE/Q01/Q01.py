from prettytable import PrettyTable


class Comentario:
    id = 0

    def __init__(self, conteudo, curtida, apoio, riso, raiva) -> None:
        self.id = Comentario.id
        Comentario.id += 1
        self.conteudo = conteudo
        self.curtida = curtida
        self.apoio = apoio
        self.riso = riso
        self.raiva = raiva


class NodeCometario:
    def __init__(self, comentario: Comentario) -> None:
        self.comentario = comentario
        self.right = None
        self.left = None


class ComentarioTree:
    def __init__(self) -> None:
        self.root = None
        self.root_curtida = None
        self.root_apoio = None
        self.root_riso = None
        self.root_raiva = None

    def insert(self, comentario: Comentario):
        self.insert_content(comentario)
        self.insert_likes(comentario)
        self.insert_apoio(comentario)
        self.insert_risos(comentario)
        self.insert_raiva(comentario)

    def insert_content(self, comentario: Comentario):
        new_comentario = NodeCometario(comentario)
        if self.root == None:
            self.root = new_comentario
            return

        node = self.root
        while node:
            if new_comentario.comentario.conteudo < node.comentario.conteudo:
                if node.left == None:
                    node.left = new_comentario
                    return
                node = node.left
            elif new_comentario.comentario.conteudo > node.comentario.conteudo:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right
            else:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right

    def display_by_content(self):
        root = self.root
        tabela = PrettyTable()

        tabela.title = "Comentários em Ordem de Conteudo"

        # Aqui eu defino os nomes das colunas
        tabela.field_names = [
            "id",
            "Conteudo",
            "Curtidas",
            "Apoio",
            "Risos",
            "Raiva",
        ]

        self.em_ordem(root, tabela)
        print(tabela, end="\n\n")

    def insert_likes(self, comentario: Comentario):
        new_comentario = NodeCometario(comentario)
        if self.root_curtida == None:
            self.root_curtida = new_comentario
            return

        node = self.root_curtida
        while node:
            if new_comentario.comentario.curtida > node.comentario.curtida:
                if node.left == None:
                    node.left = new_comentario
                    return
                node = node.left
            elif new_comentario.comentario.curtida < node.comentario.curtida:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right
            else:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right

    def insert_apoio(self, comentario: Comentario):
        new_comentario = NodeCometario(comentario)
        if self.root_apoio == None:
            self.root_apoio = new_comentario
            return

        node = self.root_apoio
        while node:
            if new_comentario.comentario.apoio > node.comentario.apoio:
                if node.left == None:
                    node.left = new_comentario
                    return
                node = node.left
            elif new_comentario.comentario.apoio < node.comentario.apoio:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right
            else:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right

    def insert_risos(self, comentario: Comentario):
        new_comentario = NodeCometario(comentario)
        if self.root_riso == None:
            self.root_riso = new_comentario
            return

        node = self.root_riso
        while node:
            if new_comentario.comentario.riso > node.comentario.riso:
                if node.left == None:
                    node.left = new_comentario
                    return
                node = node.left
            elif new_comentario.comentario.riso < node.comentario.riso:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right
            else:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right

    def insert_raiva(self, comentario: Comentario):
        new_comentario = NodeCometario(comentario)
        if self.root_raiva == None:
            self.root_raiva = new_comentario
            return

        node = self.root_raiva
        while node:
            if new_comentario.comentario.raiva > node.comentario.raiva:
                if node.left == None:
                    node.left = new_comentario
                    return
                node = node.left
            elif new_comentario.comentario.raiva < node.comentario.raiva:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right
            else:
                if node.right == None:
                    node.right = new_comentario
                    return
                node = node.right

    def display_by_likes(self):
        root = self.root_curtida
        tabela = PrettyTable()

        tabela.title = "Comentários em Ordem de Curtidas"

        # Aqui eu defino os nomes das colunas
        tabela.field_names = [
            "id",
            "Conteudo",
            "Curtidas",
            "Apoio",
            "Risos",
            "Raiva",
        ]

        self.em_ordem(root, tabela)
        print(tabela, end="\n\n")

    def display_by_support(self):
        root = self.root_apoio
        tabela = PrettyTable()

        tabela.title = "Comentários em Ordem de Apoio"

        # Aqui eu defino os nomes das colunas
        tabela.field_names = [
            "id",
            "Conteudo",
            "Curtidas",
            "Apoio",
            "Risos",
            "Raiva",
        ]

        self.em_ordem(root, tabela)
        print(tabela, end="\n\n")

    def display_by_laugh(self):
        root = self.root_riso
        tabela = PrettyTable()

        tabela.title = "Comentários em Ordem de Risos"

        # Aqui eu defino os nomes das colunas
        tabela.field_names = [
            "id",
            "Conteudo",
            "Curtidas",
            "Apoio",
            "Risos",
            "Raiva",
        ]

        self.em_ordem(root, tabela)
        print(tabela, end="\n\n")

    def display_by_anger(self):
        root = self.root_raiva
        tabela = PrettyTable()

        tabela.title = "Comentários em Ordem de Raiva"

        # Aqui eu defino os nomes das colunas
        tabela.field_names = [
            "id",
            "Conteudo",
            "Curtidas",
            "Apoio",
            "Risos",
            "Raiva",
        ]

        self.em_ordem(root, tabela)
        print(tabela, end="\n\n")

    def em_ordem(self, raiz, tabela):
        if not raiz:
            return

        # Visita filho da esquerda.
        self.em_ordem(raiz.left, tabela)

        # Visita nodo corrente.
        # e aqui ele vai preenchendo as linhas dentro do for
        tabela.add_row(
            [
                raiz.comentario.id,
                raiz.comentario.conteudo,
                raiz.comentario.curtida,
                raiz.comentario.apoio,
                raiz.comentario.riso,
                raiz.comentario.raiva,
            ]
        )
        # print(f"{raiz.comentario.conteudo} - {raiz.comentario.curtida}")

        # Visita filho da direita.
        self.em_ordem(raiz.right, tabela)

    def print_tree(self, node=None, level=0, prefix="Raiz: "):
        if node is None:
            node = self.root

        if node is not None:
            print(" " * 4 * level + prefix + str(node.comentario.conteudo))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "Esquerda--- ")
                else:
                    print(" " * 4 * (level + 1) + "Esquerda--- Vazio")
                if node.right:
                    self.print_tree(node.right, level + 1, "Direita--- ")
                else:
                    print(" " * 4 * (level + 1) + "Direita--- Vazio")


def main_menu():
    postagem = ComentarioTree()

    while True:
        print("\n=== Menu Principal de Comentários ===")
        print("1 - Inserir um novo comentário")
        print("2 - Exibir todos os comentários por conteúdo")
        print("3 - Exibir comentários ordenados por curtidas")
        print("4 - Exibir comentários ordenados por apoio")
        print("5 - Exibir comentários ordenados por risos")
        print("6 - Exibir comentários ordenados por raiva")
        print("7 - Imprimir árvore de comentários")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conteudo = input("Digite o conteúdo do comentário: ")
            curtida = int(input("Número de curtidas: "))
            apoio = int(input("Número de apoios: "))
            riso = int(input("Número de risos: "))
            raiva = int(input("Número de raivas: "))
            comentario = Comentario(conteudo, curtida, apoio, riso, raiva)
            postagem.insert(comentario)
            print("Comentário inserido com sucesso!")
        elif opcao == "2":
            postagem.display_by_content()
        elif opcao == "3":
            postagem.display_by_likes()
        elif opcao == "4":
            postagem.display_by_support()
        elif opcao == "5":
            postagem.display_by_laugh()
        elif opcao == "6":
            postagem.display_by_anger()
        elif opcao == "7":
            postagem.print_tree()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main_menu()
