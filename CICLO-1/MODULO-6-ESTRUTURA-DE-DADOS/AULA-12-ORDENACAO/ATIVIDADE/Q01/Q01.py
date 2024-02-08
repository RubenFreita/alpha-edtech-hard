filmes_recomendados = [
    {"titulo": "Inception", "ano": 2010, "relevancia": 98},
    {"titulo": "Interstellar", "ano": 2014, "relevancia": 99},
    {"titulo": "The Matrix", "ano": 1999, "relevancia": 97},
    {"titulo": "The Social Network", "ano": 2010, "relevancia": 96},
    {"titulo": "Pulp Fiction", "ano": 1994, "relevancia": 95},
    {"titulo": "The Dark Knight", "ano": 2008, "relevancia": 99},
    {"titulo": "Fight Club", "ano": 1999, "relevancia": 98},
    {"titulo": "Forrest Gump", "ano": 1994, "relevancia": 97},
    {"titulo": "Inglourious Basterds", "ano": 2009, "relevancia": 96},
    {"titulo": "The Prestige", "ano": 2006, "relevancia": 95},
    {"titulo": "Django Unchained", "ano": 2012, "relevancia": 95},
    {"titulo": "The Irishman", "ano": 2019, "relevancia": 98},
]

# Escolhendo o algoritmo de ordenação
# A escolha do algoritmo de ordenação é crucial para garantir performance e eficiência.
# Neste caso, optaremos pelo mergesort, que é estável e tem complexidade O(n log n)
# tanto no melhor quanto no pior caso.
# A estabilidade é importante aqui porque queremos manter a ordem relativa de filmes
# com a mesma pontuação de relevância
# mas com anos de lançamento diferentes, o que o mergesort garante.


def ordenar_filmes(lista_filmes):
    """
    Ordena uma lista de filmes pela pontuação de relevância de forma decrescente.
    Em caso de empate na pontuação de relevância, ordena de forma decrescente pelo ano de lançamento.
    Utiliza mergesort para garantir eficiência e estabilidade na ordenação.
    """

    # Função de ordenação baseada em mergesort adaptada para os critérios específicos
    def merge_sort(filmes):
        if len(filmes) > 1:
            meio = len(filmes) // 2
            esquerda = filmes[:meio]
            direita = filmes[meio:]

            merge_sort(esquerda)
            merge_sort(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                # o if faz a ordenação pela relevância do filme e se por acaso a relevância
                # for igual ele faz a ordenação pelo ano de lançamento.
                if esquerda[i]["relevancia"] > direita[j]["relevancia"] or (
                    esquerda[i]["relevancia"] == direita[j]["relevancia"]
                    and esquerda[i]["ano"] > direita[j]["ano"]
                ):
                    filmes[k] = esquerda[i]
                    i += 1
                else:
                    filmes[k] = direita[j]
                    j += 1
                k += 1

            while i < len(esquerda):
                filmes[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                filmes[k] = direita[j]
                j += 1
                k += 1

    merge_sort(lista_filmes)
    return lista_filmes


ordenados = ordenar_filmes(filmes_recomendados)
print(ordenados)
