
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def __enter__(self):
        print("Entrou na classe Pessoa!!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo da classe Pessoa!!")

if __name__ == "__main__":
    with Pessoa("Ruben", 24) as ruben:
        print(ruben.nome)
        print(ruben.idade)
