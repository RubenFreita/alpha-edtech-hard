import json


class RedeEnergetica:
    def __init__(self):
        self.grafo = {
            "Empresa": ["Solar", "Eolica", "Fossil"],
            "Solar": ["S1", "S2", "S3"],
            "Eolica": ["E4", "E5"],
            "Fossil": ["F6", "F7"],
            "S1": [],
            "S2": [],
            "S3": [],
            "E4": [],
            "E5": [],
            "F6": [],
            "F7": [],
        }
        self.total_emissoes = {"Empresa": 0, "Solar": 0, "Eolica": 0, "Fossil": 0}

    def calcular_emissoes(self, ponto, energia_produzida, fator_emissao):
        # DESENVOLVA O MÉTODO PARA CÁLCULO DAS EMISSÕES
        if ponto not in self.total_emissoes:
            self.total_emissoes[ponto] = 0
        self.total_emissoes[ponto] += energia_produzida * fator_emissao
        for origem, destinos in self.grafo.items():
            if ponto in destinos:
                self.calcular_emissoes(origem, energia_produzida, fator_emissao)


# Exemplo de dados: Tipo de usina, produção anual em GWh, fator de emissão (toneladas de CO2 por GWh)
usinas = [
    ("Solar", 120, 0),
    ("Eólica", 200, 0),
    ("Fóssil", 500, 0.7),
]
energetica = RedeEnergetica()

energetica.calcular_emissoes("S1", 50, 0)  # Energia solar tem emissão zero
energetica.calcular_emissoes("S2", 20, 0)  # Energia solar tem emissão zero
energetica.calcular_emissoes("S3", 10, 0)  # Energia solar tem emissão zero
energetica.calcular_emissoes("E4", 40, 0)  # Energia eólica tem emissão zero
energetica.calcular_emissoes("E5", 50, 0)  # Energia eólica tem emissão zero
energetica.calcular_emissoes("F6", 50, 0.7)  # Energia fóssil tem alto fator de emissão
energetica.calcular_emissoes("F7", 50, 0.7)  # Energia fóssil tem alto fator de emissão

print("Total de emissões de carbono: ")
print(json.dumps(energetica.total_emissoes, indent=4))
