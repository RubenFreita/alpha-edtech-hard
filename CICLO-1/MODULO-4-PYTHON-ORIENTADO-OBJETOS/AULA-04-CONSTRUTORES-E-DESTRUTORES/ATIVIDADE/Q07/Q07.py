
class Pessoa:
    def __init__(self, nome, idade, endereco) -> None:
        self.nome = nome
        if isinstance(idade, int):
            self.idade = idade
        elif isinstance(idade, str):
            try:
                self.idade = int(idade)
            except:
                print("Não foi possível converter a idade para inteiro.")
        else:
            print("Idade fornecida de forma desconhecida.")
        self.endereco = endereco
    
if __name__ == "__main__":
    ruben = Pessoa("Ruben", 24, "Rua Pereiras, 09")
    print(ruben.__dict__)

    gabriel = Pessoa("Gabriel", "18", "Centro, 109")
    print(gabriel.__dict__)

    alice = Pessoa("Alice", "a", "13 de maio, 1459")
    print(alice.__dict__)