class Paralelepipedo:

    # Implementar método construtor
    def __init__(self, largura: float = 0.15, comprimento: float = 0.25, profundidade: float = 0.10):
        self.largura = largura
        self.comprimento = comprimento
        self.profundidade = profundidade

    # Implementar método imprimir
    def __str__(self) -> str:
        return f"forma= {self.largura} x {self.comprimento} x {self.profundidade}"


tijolo1 = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo1: ", tijolo1)

tijolo2 = Paralelepipedo()
print("tijolo2: ", tijolo2)
