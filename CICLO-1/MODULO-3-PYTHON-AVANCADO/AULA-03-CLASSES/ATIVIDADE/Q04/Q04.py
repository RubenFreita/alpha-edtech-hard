from typing import List

class Professor:
    def __init__(self, nome: str, especialista: str):
        self.nome = nome
        self.especialista = especialista

def imprime_professores(professores: List[Professor]) -> None:
    for i in professores:
        print(f"Professor {i.nome} especialista em {i.especialista}.")


# Lista de produtos
professores: List[Professor] = [
    Professor("Marcotti", "Python"),
    Professor("Kenji", "JavaScript"),
    Professor("Zanetti", "Git"),
    Professor("Diogo", "Análise de Dados"),
    Professor("Vitor", "JavaScript"),
    #"Samir" #Este item dará erro pois a lista espera receber apenas instâncias de Professores
]
"""
Podemos ver que se deixar a string descomentada o mypy irá aponar um erro de tipo 
durante a execução do algoritmo, isso demonstra um erro de tipagem, pois a lista
é do tipo Professor, sendo assim só aceita objetos do tipo Professor.
"""

print("Mostrando os professores e suas especializações!")
print()
imprime_professores(professores)
