import random
from .produto import Produto


class ListaModificada(list):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def ordena_id(self):
        aux = sorted(self, key=lambda x: x["produto"].id)
        self.clear()
        for i in aux:
            self.append(i)

    def ordena_nome(self):
        aux = sorted(self, key=lambda x: x["produto"].nome.lower())
        self.clear()
        for i in aux:
            self.append(i)

    def desordena(self):
        aux = ListaModificada(self.copy())
        self.clear()
        for i in aux:
            self.insert(random.randint(0, int(len(self))), i)

    def busca_binaria(self, nome_produto: str):
        self.ordena_nome()
        ini, fim = 0, len(self)
        while ini < fim:
            meio = (ini + fim) // 2

            if nome_produto.lower() == self[meio]["produto"].nome.lower():
                # return self[meio]["produto"].nome
                return f"\nValor encontrado no indice {meio}"
            elif nome_produto.lower() < self[meio]["produto"].nome.lower():
                fim = meio - 1
            else:
                ini = meio + 1
        return "Não encontrado"


if __name__ == "__main__":
    arroz = Produto("arroz", 4.5)
    macarrao = Produto("macarrao", 4.5)
    feijao = Produto("feijao", 4.5)
    carne = Produto("carne", 4.5)
    frango = Produto("frango", 4.5)

    lista = ListaModificada(
        [{"quantidade": 1, "produto": arroz}, {"quantidade": 2, "produto": macarrao}]
    )
    lista.append({"quantidade": 3, "produto": feijao})
    lista.append({"quantidade": 4, "produto": carne})
    lista.append({"quantidade": 5, "produto": frango})
    print(lista)

    lista.desordena()
    print(lista)
    lista.ordena_id()

    print(lista)
