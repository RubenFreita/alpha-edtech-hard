import time


class BibliotecaOrdenada:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros de forma ordenada

    def adicionar_livro(self, titulo):
        # Encontra a posição correta para inserir o livro de forma ordenada
        index = 0
        while index < len(self.livros) and self.livros[index] < titulo:
            index += 1
        self.livros.insert(index, titulo)
        print(f"O livro '{titulo}' foi adicionado à biblioteca.")

    def listar_livros(self):
        if self.livros:
            print("Livros na Biblioteca (Ordenados):")
            for livro in self.livros:
                print(f"- {livro}")
        else:
            print("A biblioteca está vazia.")

    def remover_livro(self, titulo):
        if titulo in self.livros:
            self.livros.remove(titulo)
            print(f"O livro '{titulo}' foi removido da biblioteca.")
        else:
            print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

    def busca_binaria(self, titulo):
        ini, fim = 0, len(self.livros) - 1

        while ini < fim:
            meio = (ini + fim) // 2
            alvo_meio = self.livros[meio]
            if alvo_meio.lower() == titulo.lower():
                return meio
            elif titulo < alvo_meio:
                fim = meio - 1
            else:
                ini = meio + 1
        return -1


titulos_livros = [
    "Dom Quixote",
    "1984",
    "Ulisses",
    "O Grande Gatsby",
    "Em Busca do Tempo Perdido",
    "Cem Anos de Solidão",
    "Guerra e Paz",
    "O Processo",
    "Lolita",
    "A Divina Comédia",
    "Crime e Castigo",
    "Os Irmãos Karamazov",
    "O Apanhador no Campo de Centeio",
    "O Sol é Para Todos",
    "O Senhor dos Anéis",
    "Moby Dick",
    "Orgulho e Preconceito",
    "Jane Eyre",
    "Morro dos Ventos Uivantes",
    "Passagem para a Índia",
    "Para Matar a Cotovia",
    "Admirável Mundo Novo",
    "Fahrenheit 451",
    "Grande Sertão: Veredas",
    "A Metamorfose",
    "Cem Sonetos de Amor",
    "A Hora da Estrela",
    "Capitães da Areia",
    "Vidas Secas",
    "Dom Casmurro",
    "Memórias Póstumas de Brás Cubas",
    "O Alquimista",
    "A Cidade e os Cachorros",
    "O Nome da Rosa",
    "Ensaio Sobre a Cegueira",
    "O Velho e o Mar",
    "A Insustentável Leveza do Ser",
    "Sagarana",
    "A Moreninha",
    "Iracema",
    "O Guarani",
    "Memórias de um Sargento de Milícias",
    "Quincas Borba",
    "O Primo Basílio",
    "O Alienista",
    "Senhora",
    "A Escrava Isaura",
    "Os Sertões",
    "Macunaíma",
    "O Tempo e o Vento",
]

if __name__ == "__main__":
    biblioteca = BibliotecaOrdenada()

    for livro in titulos_livros:
        biblioteca.adicionar_livro(livro)

    titulo1 = "ulisses"

    tempo_inicial = time.time()
    indice1 = biblioteca.busca_binaria(titulo1)
    tempo_final = time.time()

    if indice1 == -1:
        print("\nTitulo Não Encontrado")
    else:
        print(f"\nTítuto encontrado: {biblioteca.livros[indice1]}")

    print(
        f"O tempo de busca do título {titulo1} foi de {tempo_final-tempo_inicial:.20f} segundos"
    )

    titulo2 = "O Nome da Rosa"
    tempo_inicial = time.time()

    indice2 = biblioteca.busca_binaria(titulo2)

    tempo_final = time.time()

    if indice2 == -1:
        print("\nTitulo Não Encontrado")
    else:
        print(f"\nTítuto encontrado: {biblioteca.livros[indice2]}")

    print(
        f"O tempo de busca do título {titulo2} foi de {tempo_final-tempo_inicial:.20f} segundos"
    )
