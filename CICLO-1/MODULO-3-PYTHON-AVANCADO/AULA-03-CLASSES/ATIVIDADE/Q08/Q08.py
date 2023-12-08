


dados_variados = [42, "hello", 3.14, [1, 2, 3], {'nome': 'Alice', 'idade': 25}, True, (10, 20, 30), None]


def imprime_de_acordo_com_tipo(lista):
    for item in lista:
        if isinstance(item, int):
            print(f"Inteiro encontrado: {item}")
        elif isinstance(item, str):
            print(f"String encontrada: {item}")
        elif isinstance(item, float):
            print(f"Float encontrado: {item}")
        elif isinstance(item, list):
            print(f"Lista encontrada: {item}")
        elif isinstance(item, dict):
            print(f"Dicionário encontrado: {item}")
        elif isinstance(item, bool):
            print(f"Booleano encontrado: {item}")
        elif isinstance(item, tuple):
            print(f"Tupla encontrada: {item}")
        else:
            print(f"Tipo de dado não identificado: {item}")

imprime_de_acordo_com_tipo(dados_variados)