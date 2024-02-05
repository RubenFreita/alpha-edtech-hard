import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = []

    def add_edge(self, from_vertex, to_vertex, distance, speed):
        # A aresta agora inclui a velocidade
        self.vertices[from_vertex].append((to_vertex, distance, speed))

    def dijkstra(self, start_vertex, mode="distance"):
        distances = {vertex: float("infinity") for vertex in self.vertices}
        previous_vertices = {vertex: None for vertex in self.vertices}
        distances[start_vertex] = 0
        pq = [(0, start_vertex)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            for neighbor, distance, speed in self.vertices[current_vertex]:
                if mode == "distance":
                    new_distance = current_distance + distance
                elif mode == "speed":
                    # Supondo que a velocidade é em unidades por hora e a distância em unidades,
                    # calculamos o tempo necessário para percorrer essa aresta e usamos como "distância"
                    time = distance / speed
                    new_distance = current_distance + time

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))

        return distances, previous_vertices

    def get_shortest_path(self, start_vertex, target_vertex, mode="distance"):
        distances, predecessors = self.dijkstra(start_vertex, mode)
        path = []
        current_vertex = target_vertex

        if distances[target_vertex] == float("infinity"):
            return "Não existe caminho de {} para {}".format(
                start_vertex, target_vertex
            )

        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        return path


# Exemplo de uso
g = Graph()
# Adicionando vértices
g.add_vertex("Depósito")
g.add_vertex("Ponto A")
g.add_vertex("Ponto B")
g.add_vertex("Ponto C")
g.add_vertex("Ponto D")

# Adicionando arestas com velocidade
g.add_edge("Depósito", "Ponto A", 5, 60)
g.add_edge("Depósito", "Ponto B", 10, 50)
g.add_edge("Ponto A", "Ponto C", 15, 40)
g.add_edge("Ponto B", "Ponto C", 20, 70)
g.add_edge("Ponto B", "Ponto D", 30, 100)
g.add_edge("Ponto C", "Depósito", 30, 80)
g.add_edge("Ponto C", "Ponto D", 15, 55)
g.add_edge("Ponto D", "Ponto C", 10, 65)


def main_menu(graph):
    print("Escolha o critério para encontrar o caminho:")
    print("1 - Menor distância")
    print("2 - Maior velocidade")
    opcao = input("Opção: ")

    print("\nEscolha uma das opções como ponto de inicio e destino!")
    print("1 - Depósito")
    print("2 - Ponto A")
    print("3 - Ponto B")
    print("4 - Ponto C")
    print("5 - Ponto D")

    opcao_start = input("Ponto de início: ")
    if opcao_start == "1":
        start = "Depósito"
    elif opcao_start == "2":
        start = "Ponto A"
    elif opcao_start == "3":
        start = "Ponto B"
    elif opcao_start == "4":
        start = "Ponto C"
    elif opcao_start == "5":
        start = "Ponto D"
    opcao_end = input("Ponto de destino: ")
    if opcao_end == "1":
        end = "Depósito"
    elif opcao_end == "2":
        end = "Ponto A"
    elif opcao_end == "3":
        end = "Ponto B"
    elif opcao_end == "4":
        end = "Ponto C"
    elif opcao_end == "5":
        end = "Ponto D"

    if opcao == "1":
        print(f"Menor caminho de {start} para {end} baseado em distância:")
        print(graph.get_shortest_path(start, end, "distance"))
    elif opcao == "2":
        print(f"Caminho mais rápido de {start} para {end} baseado em velocidade:")
        print(graph.get_shortest_path(start, end, "speed"))
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main_menu(g)
