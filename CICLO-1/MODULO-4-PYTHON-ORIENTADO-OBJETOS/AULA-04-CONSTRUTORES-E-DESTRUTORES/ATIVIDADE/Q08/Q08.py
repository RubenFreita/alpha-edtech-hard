class Anime:

    # Aloca memória dinamicamente
    melhores_animes = ["Naruto", "One Piece", "Tokyo Revengers"]

    def __init__(self, nome):
        # Aloca memória dinamicamente
        self.nome = nome
        print(f"INFO: Objeto {self.nome}, foi criado.")
        
    def adiciona_melhores(self):
        self.melhores_animes.append(self.nome)


    def __del__(self):
        # Libera a memória alocada dinamicamente
        print(f"INFO: Objeto {self.nome}, foi destruído.")


if __name__ == "__main__":

    print("INFO: Inicio de Programa.")

    jujutsu = Anime("Jujutsu")
    bleach = Anime("Bleach")

    del bleach
    del jujutsu

    print("INFO: Fim de Programa.")