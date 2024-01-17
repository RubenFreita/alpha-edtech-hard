class Carro:
    def __init__(self, modelo, cor):
        self._modelo = modelo
        self.__cor = cor

    def obter_cor(self):
        return self.__cor

    def acelerar(self):
        print(f"O carro {self._modelo} esta acelerando!")


meu_carro = Carro("Sedan", "Prata")
print(meu_carro.obter_cor())
print(meu_carro.__cor)
