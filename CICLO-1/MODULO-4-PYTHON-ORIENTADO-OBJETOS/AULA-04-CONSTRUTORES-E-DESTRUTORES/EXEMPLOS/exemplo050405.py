class Paralelepipedo:

    # Implementar método construtor
    def __init__(self, largura, comprimento, profundidade):
        self.largura = largura
        self.comprimento = comprimento
        self.profundidade = profundidade

    # Implementar método imprimir
    def __str__(self) -> str:
        return f"forma= {self.largura} x {self.comprimento} x {self.profundidade}"


tijoloBarro1 = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo 1: ", tijoloBarro1)

tijoloBarro2 = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo 2: ", tijoloBarro2)

x = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo 3: ", x)

bloco1 = Paralelepipedo(0.2, 0.4, 0.15)
print("bloco 1: ", bloco1)
