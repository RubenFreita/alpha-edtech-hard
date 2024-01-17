class Anime:

    # Aloca memória dinamicamente
    melhores_animes = ["Naruto", "One Piece", "Tokyo Revengers"]

    def __init__(self, nome):
        # Aloca memória dinamicamente
        self.nome = nome
        print("Criando objeto anime")
        
    def adiciona_melhores(self):
        self.melhores_animes.append(self.nome)


    def __del__(self):
        # Libera a memória alocada dinamicamente
        print("Objeto destruído.")



if __name__ == "__main__":
    jujutsu = Anime("Jujutsu")

    jujutsu.adiciona_melhores()

    print(jujutsu.melhores_animes)