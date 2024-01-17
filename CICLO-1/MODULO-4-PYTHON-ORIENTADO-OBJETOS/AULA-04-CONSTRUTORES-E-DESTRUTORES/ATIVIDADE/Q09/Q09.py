
class Animal:

    def __init__(self, nome, idade = 1, classe = "Mamífero", sub_classe = "terrestre",) -> None:
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.sub_classe = sub_classe

if __name__ == "__main__":

    urso = Animal("Pool")
    print(urso.__dict__)

    picapau = Animal("Pica Pau amarelo", idade= 2, classe = "Ave", sub_classe=None)
    print(picapau.__dict__)

    baleia = Animal("Baleia Azul", sub_classe= "Aquático")
    print(baleia.__dict__)