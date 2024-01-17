class Paralelepipedo:
    qtdParalelepipedo = 0 # Atributo da Classe e não de cada objeto

    def __init__(self, largura: float = 0.15, comprimento: float = 0.25, profundidade: float = 0.10):
        self.largura = largura # Atributo de Instância
        self.comprimento = comprimento
        self.profundidade = profundidade
        Paralelepipedo.qtdParalelepipedo += 1

    # def __str__(self) -> str:
    #     return f"forma= {self.largura} x {self.comprimento} x {self.profundidade}"


tijolo1 = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo1: ", tijolo1)

print(tijolo1)
print(type(tijolo1))

tijolo2 = Paralelepipedo(0.35, 0.45, 0.20)
# tijolo2 = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo2: ", tijolo2)

print(tijolo1.__dict__)
print(tijolo2.__dict__)
