# Definindo a classe Pessoa que usa a classe Endereco como atributo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


# Criando instâncias da classe Pessoa com diferentes endereços
pessoa1 = Pessoa("Magno", 25)
pessoa2 = Pessoa("Bianca", 18)
pessoa3 = Pessoa("Deivid", 36)

# Exibindo informações das instâncias
print(pessoa1)
print(pessoa2)
print(pessoa3)
