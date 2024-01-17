class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass


class Cachorro(Animal):
    __raca = "viralata"

    def __init__(self, nome):
        super().__init__(nome)

    @property
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, new_raca):
        self.__raca = new_raca

    def fazer_som(self):
        return "Au au!"

    def abanar_rabo(self):
        return "Cachorro está abanando o rabo!"

class Husky(Cachorro):
    def __init__(self, nome):
        super().__init__(nome)

    @property
    def raca(self):
        pass
    
    
    


dog = Cachorro("dog")
print(dog.raca)
dog.raca = "caramelo"
print(dog.raca)


kira = Husky("Kira")
print(kira.raca) 
kira.raca = "husky + caramelo"
print(kira.raca) 

# print(kira.racao)



