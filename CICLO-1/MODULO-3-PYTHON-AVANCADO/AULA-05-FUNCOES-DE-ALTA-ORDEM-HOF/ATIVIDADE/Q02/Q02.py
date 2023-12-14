
from typing import Callable

def cria_formatacao(vogal: str, simbolo: str) -> Callable[[str], str]:

    def troca_vogal_por_simbolo(palavra: str) -> str:
        nova_palavra = []
        for i in palavra:
            if i.lower() == vogal.lower():
                nova_palavra.append(simbolo)
            else:
                nova_palavra.append(i)
        return "".join(nova_palavra)
    return troca_vogal_por_simbolo

troca_a_por_arroba = cria_formatacao("a", "@")
troca_e_por_3 = cria_formatacao("e", "3")

cripto1 = troca_a_por_arroba("sabonete")
print(cripto1)
cripto2 = troca_e_por_3(cripto1)
print(cripto2)