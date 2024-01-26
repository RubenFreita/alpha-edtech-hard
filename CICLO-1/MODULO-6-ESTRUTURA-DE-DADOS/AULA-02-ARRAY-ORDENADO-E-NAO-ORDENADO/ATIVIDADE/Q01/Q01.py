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

    biblioteca.listar_livros()
