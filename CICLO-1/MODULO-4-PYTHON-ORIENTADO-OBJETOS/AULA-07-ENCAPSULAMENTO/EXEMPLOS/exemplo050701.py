class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def acelerar(self):
        print(f"O carro {self.modelo} esta acelerando!")


meu_carro = Carro("Sedan", "Prata")
meu_carro.acelerar()
