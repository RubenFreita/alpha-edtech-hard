from typing import List

#função impura porque pode retornar pois o retorno não
#é determinístico, pois não sabemos quantas palavras serão
#adicionadas pelo usuário
def get_user_words() -> List[str]:
    print("Informe quantas palavras quer inserir: ")
    quant = int(input())
    palavras = []
    for i in range(quant):
        palavra = input("Informe uma palavra: ")
        palavras.append(palavra)
    return palavras

#funcão pura
def count_x_occurrences(word: str) -> int:
    count = 0
    for i in word:
        if i.lower() == "x":
            count += 1
    return count

#funcão pura
def calculate_average(palavras: List[str]) -> float:
    ocorrencias_x = []
    for i in palavras:
        ocorrencias_x.append(count_x_occurrences(i))
    return round(sum(ocorrencias_x)/len(ocorrencias_x), 2)

#funcão pura
def inform_average(average: float) -> None:
    print(f"A média de ocorrências de x na lista de palavras é: {average}")

media = calculate_average(get_user_words())
inform_average(media)