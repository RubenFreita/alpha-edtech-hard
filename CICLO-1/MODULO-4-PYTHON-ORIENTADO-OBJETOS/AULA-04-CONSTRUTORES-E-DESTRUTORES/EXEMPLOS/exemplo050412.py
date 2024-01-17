class Paralelepipedo:
    qtdParalelepipedo = 0 # Atributo da Classe e não de cada objeto

    def __init__(self, largura: float = 0.15, comprimento: float = 0.25, profundidade: float = 0.10):
        self.largura = largura # Atributo de Instância
        self.comprimento = comprimento
        self.profundidade = profundidade
        Paralelepipedo.qtdParalelepipedo += 1

    def __str__(self) -> str:
        return f"forma= {self.largura} x {self.comprimento} x {self.profundidade}"


tijolo1 = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo1: ", tijolo1)

tijolo2 = Paralelepipedo()
print("tijolo2: ", tijolo2)

print(Paralelepipedo.qtdParalelepipedo)

tijolo = []
for i in range(10):
    nomeArq = "Tijolo" + str(i)
    tijolo.append(Paralelepipedo(0.15, 0.25, 0.10))
print(Paralelepipedo.qtdParalelepipedo)
