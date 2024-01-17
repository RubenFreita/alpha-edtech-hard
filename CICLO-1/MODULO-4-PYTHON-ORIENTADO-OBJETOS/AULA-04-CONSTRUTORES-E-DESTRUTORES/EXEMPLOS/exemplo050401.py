class Paralelepipedo:
    largura: float
    comprimento: float
    profundidade: float

    # Implementar método construtor
    def __init__(self) -> None:
        pass

    def multiplicar(self, fator=100) -> None:
        self.largura *= (1.0+fator/100.0)

    # Implementar método imprimir
    def __str__(self) -> str:
        pass


tijolo = Paralelepipedo(0.15, 0.25, 0.10)
bloco = tijolo.multiplicar(50)
