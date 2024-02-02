from collections import deque


class Graph:
    def __init__(self) -> None:
        self.list_adjacent = dict()

    def insert_edge(self, init, end):
        if init not in self.list_adjacent:
            self.list_adjacent[init] = []
        if end not in self.list_adjacent:
            self.list_adjacent[end] = []

        self.list_adjacent[init].append(end)

    def search_bfs(self, init):
        queue = deque([init])
        visited = set()

        visited.add(init)
        print(f"\nOrdem de visita dos vértices: ")
        i = 1
        print(f"{i}° -> {init}")

        while queue:
            current_vertex = queue.popleft()
            for vertex in self.list_adjacent[current_vertex]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
                    i += 1
                    print(f"{i}° -> {vertex}")

    def display_list_adjacent(self):
        for vertice, value in self.list_adjacent.items():
            print(f"Vertice {vertice} ->", end=" ")
            for aresta in value:
                print(f"{aresta}", end=" ")
            print()


if __name__ == "__main__":
    g = Graph()

    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(1, 2)
    g.insert_edge(2, 0)
    g.insert_edge(2, 3)
    g.insert_edge(3, 3)

    g.display_list_adjacent()
    g.search_bfs(2)
