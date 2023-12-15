from typing import List, Callable

frases_naruto = [
    "Trabalho duro é inútil para aqueles que não acreditam em si mesmos",
    "Lar é onde tem alguém sempre pensando em você",
    "Desista de me fazer desistir",
    "Quando eu não tinha nada nem ninguém, eu tinha a dor",
    "Aqueles que não entendem a verdadeira dor nunca vão entender a verdadeira paz",
    "Quando um homem aprende a amar, ele deve suportar o risco de ser odiado",
    "Se você se concentrar em algo, poderá fazer qualquer coisa",
    "Desde que você não desista, vai sempre existir salvação"
                ]

def tokeniza_frase(lista: List[str]) -> List[List[str]]:
    return list(map(lambda l: l.split(), lista))

def upper_tokens(lista: List[List[str]]) -> List[List[str]]:
    return list(map(lambda l: list(map(lambda p: p.upper(), l)), lista))

def transforma_frases(lista: List[str], \
                      funcao1: Callable, funcao2: Callable) -> List[List[str]]:
    return funcao1(funcao2(lista))



frases_transformadas = transforma_frases(\
    frases_naruto, upper_tokens, tokeniza_frase)

for i in frases_transformadas:
    print(i)


"""
[token for item in lista for token in re.sub(r"\W","",item).split()]
\W pega tudo que não é alpha númerico, muito bom para retirar coisas alphanúmerico
"""