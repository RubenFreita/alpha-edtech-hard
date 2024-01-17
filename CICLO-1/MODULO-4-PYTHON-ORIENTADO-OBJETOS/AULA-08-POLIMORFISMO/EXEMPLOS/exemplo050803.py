class Animal:
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


def emitir_som(animal):
       return animal.fazer_som()


cachorro = Cachorro()
gato = Gato()

print(emitir_som(cachorro))  # Saída: Au au!
print(emitir_som(gato))      # Saída: Miau!
