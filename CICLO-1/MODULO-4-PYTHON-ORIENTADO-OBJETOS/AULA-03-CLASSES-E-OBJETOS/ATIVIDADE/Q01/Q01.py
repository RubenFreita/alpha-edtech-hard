class Autor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Livro:
    def __init__(self, titulo, ano, autores):
        self.titulo = titulo
        self.ano = ano
        self.autores = []  # Associação com a classe Autor
        self.adicionar_autores(autores)

    def adicionar_autores(self, autores):
        for autor in autores:
            self.autores.append(autor)

    def listar_autores(self):
        return [autor.nome for autor in self.autores]

# Criando instâncias de Autor
autor1 = Autor(nome="J.K. Rowling", idade=56)
autor2 = Autor(nome="J.R.R. Tolkien", idade=81)

# Criando instância de Livro associada a autores
livro1 = Livro(titulo="Harry Potter", ano=1997, autores=[autor1])
livro2 = Livro(titulo="O Senhor dos Anéis", ano=1954, autores=[autor2])

# Adicionando mais autores a um livro existente
autor3 = Autor(nome="C.S. Lewis", idade=64)
livro2.adicionar_autores([autor3])

# Exibindo informações dos livros e seus autores
print(f"{livro1.titulo} foi escrito por: {livro1.listar_autores()}")
print(f"{livro2.titulo} foi escrito por: {livro2.listar_autores()}")
