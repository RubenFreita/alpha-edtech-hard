# Definindo a classe Endereco
class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.rua}, {self.cidade}, {self.estado}"


# Definindo a classe Pessoa que usa a classe Endereco como atributo
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco  # Usando a classe Endereco como atributo

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, morando em {self.endereco}"


# Criando instâncias da classe Endereco
endereco1 = Endereco("Av Barao do Rio Branco", "Angra dos Reis", "RJ")
endereco2 = Endereco("Rua Bela Vista", "Bonito", "MS")

# Criando instâncias da classe Pessoa com diferentes endereços
pessoa1 = Pessoa("Magno", 25, endereco1)
pessoa2 = Pessoa("Bianca", 18, endereco2)

# Exibindo informações das instâncias
print(pessoa1)
print(pessoa2)
