class MusicNode:
    def __init__(self, name) -> None:
        self.name: str = name
        self.next = None
        self.next_cicle = None  # next para percorrer de forma ciclica
        self.prev = None
        self.prev_cicle = None  # prev para percorrer de forma ciclica

    # modificando o eq para ele comparar o objeto através do nome da música e
    # e do tipo de classe
    def __eq__(self, other) -> bool:
        if other != None:
            if self.name == other.name and isinstance(other, MusicNode):
                return True
            else:
                return False


class MusicPlaylist:
    def __init__(self) -> None:
        self.head = None  # primeiro da lista
        self.tail = None  # ultimo da lista
        self.current_song = None

    def add_music(self, nome):
        new_song = MusicNode(nome)  # musica nova
        # verifica se o primeiro da fila é nulo se sim
        # o head irá:
        if self.head == None:
            self.head = new_song  # receber a primeira musica que for adicionada.
            self.head.next_cicle = (
                self.head
            )  # adicionao head no seu proprio proximo ciclico
            self.head.prev_cicle = (
                self.head
            )  # adiciona o head no seu proprio anterior ciclico
            self.tail = self.head  # adiciona o head como o ultimo elemento
            self.current_song = self.head  # adiciona o head como musica atual
            return  # retorna para encerrar a primeira inserção

        # se não for a primeira inserção da playlist então será feito:
        # o anterior da nova musica recebe a ultima musica
        new_song.prev = self.tail
        # o anterior ciclico da nova musica recebe a ultima musica
        new_song.prev_cicle = self.tail
        # o proximo da nova musica recebe a primeira musica
        new_song.next_cicle = self.head
        # o anterior ciclico da primeira musica recebe o novo no
        self.head.prev_cicle = new_song
        # o proximo da ultima musica recebe a nova musica
        self.tail.next = new_song
        # o proximo ciclico da ultima musica recebe o novo no
        self.tail.next_cicle = new_song
        # A ultima musica recebe a nova musica, pois agora a ultima
        # musica adicionada será a nova musica
        self.tail = new_song

    def remove_music(self, name):
        # instancia a musica que será removido
        song_remove = MusicNode(name)
        # variavel auxiliar que recebe o head e irá
        # percorrer a lista
        song = self.head
        # while que irá percorrer a lista até que song não seja None
        while song:
            # verifica se o a música que se quer remover é igual a
            # a alguma música da lista
            if song_remove == song:
                # verifica se a musica que está tocando no momento é a
                # mesma que se quer remover
                if self.current_song == song_remove:
                    # se for verdade a musica que está tocando no momento
                    # agora será a próxima música da que se quer remover
                    self.current_song = song.next_cicle
                # verifica se a musica que se quer remover é o head
                if song_remove == self.head:
                    # se for iremos fazer com que a segunda musica da lista
                    # agora seja a primeira
                    self.head = self.head.next
                    # verifica se head não é nulo
                    if self.head != None:
                        self.head.prev = None
                        # adicionando a ultima musica no anterior ciclico do head
                        self.head.prev_cicle = self.tail
                        # adicionando o head no proximo ciclico da ultima musica
                        self.tail.next_cicle = self.head
                    # devolve a musica que foi removida
                    return song_remove

                if song_remove == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    if self.tail != None:
                        self.tail.next_cicle = self.head
                        self.head.prev_cicle = self.tail
                    return song_remove

                # se não entrar no if anterior então será feito as linhas abaixo:
                # adiciona o proximo da musica no proximo da musica anterior
                song.prev.next = song.next
                # faz o mesmo que o de cima mas na forma ciclica
                song.prev.next_cicle = song.next
                # adiciona o anterior da musica no anterior do proximo da musica
                song.next.prev = song.prev
                # faz o mesmo que o de cima mas na forma ciclica
                song.next.prev_cicle = song.prev
                # devolve a musica a ser removida
                return song
            # adiciona a proxima musica na musica atual para percorrer a lista
            song = song.next
        else:
            print(f"A música {song_remove.name} não foi encontrada na playlist")

    # dar play em alguma música em específico
    def play(self, name_song):
        song_play = MusicNode(name_song)
        song = self.head
        while song:
            if song_play == song:
                self.current_song = song
                return song
            song = song.next
        else:
            print(f"\nMúsica {name_song} nao encontrada.")

    # toca a proxima musica da playlist
    def next_song(self):
        self.current_song = self.current_song.next_cicle
        return self.current_song

    # toca a musica anterior da musica que está tocando no momento
    def previous_song(self):
        self.current_song = self.current_song.prev_cicle
        return self.current_song

    # mostra todas as musicas da playlist
    def display_playlist(self):
        last_song = self.head
        if self.head == None:
            print("A Playlist está vazia.")
        else:
            print("A seta indica qual música está tocando no momento:")
        while last_song:
            name = last_song.name
            last_song = last_song.next
            if name.lower() == self.current_song.name.lower():
                print(f" -> {name}")
            else:
                print(f"    {name}")


# menu principal
def main_menu(playlist: MusicPlaylist):
    while True:
        print("\n\n----- Music Playlist Menu -----")
        print("1. Adicionar Música")
        print("2. Remover Música")
        print("3. Tocar Próxima Música")
        print("4. Tocar Música Anterior")
        print("5. Exibir Playlist")
        print("6. Tocar Música Específica")
        print("7. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("\nNome da música para adicionar: ")
            playlist.add_music(name)
        elif choice == "2":
            name = input("\nNome da música para remover: ")
            playlist.remove_music(name)
        elif choice == "3":
            song = playlist.next_song()
            print(f"\nTocando próxima música: {song.name}")
        elif choice == "4":
            song = playlist.previous_song()
            print(f"\nTocando música anterior: {song.name}")
        elif choice == "5":
            print("\nPlaylist Atual:")
            playlist.display_playlist()
        elif choice == "6":
            name = input("\nNome da música para tocar: ")
            song = playlist.play(name)
            print(f"\nTocando música: {song.name}")
        elif choice == "7":
            print("\nSaindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    playlist = MusicPlaylist()

    main_menu(playlist)
