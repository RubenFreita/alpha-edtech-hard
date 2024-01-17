class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nota: {self.nota}")

# Criar objetos da classe Aluno utilizando o construtor com parâmetros
aluno1 = Aluno("Alice", 20, 8.5)
aluno2 = Aluno("Bob", 22, 9.0)

# Exibir informações dos alunos
print("Informações do Aluno 1:")
aluno1.exibir_informacoes()

print("\nInformações do Aluno 2:")
aluno2.exibir_informacoes()
