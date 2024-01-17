class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

    def abanar_rabo(self):
        return "Cachorro está abanando o rabo!"


animal_generico = Animal("Genérico")
print(animal_generico.fazer_som())  # Saída: None

rex = Cachorro("Rex")
print(rex.fazer_som())               # Saída: "Au au!"
print(rex.abanar_rabo())             # Saída: "Cachorro está abanando o rabo!"
