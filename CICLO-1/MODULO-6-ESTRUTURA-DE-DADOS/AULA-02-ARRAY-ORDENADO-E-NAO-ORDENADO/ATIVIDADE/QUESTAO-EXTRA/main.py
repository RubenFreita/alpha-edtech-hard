
# import sys

# sys.path.append(r'C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-6-ESTRUTURA-DE-DADOS/AULA-02/ATIVIDADE/Q01')
from models.estoque  import Estoque
from models.produto  import Produto
from utils.menu  import programa

if __name__ == "__main__":


    estoque = Estoque()

    with open("./data/lista_produtos.csv", "r") as lista:
        for i in lista:
            aux = i[0:-1].split(",")
            estoque.adicionar_produtos(Produto(aux[1], float(aux[2])), int(aux[0]))


    programa(estoque)
    