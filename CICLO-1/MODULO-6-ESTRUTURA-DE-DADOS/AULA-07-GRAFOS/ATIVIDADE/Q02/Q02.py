class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        # Como é um grafo não dirigido, adicionamos a aresta inversa também.
        if v not in self.graph:
            self.graph[v] = []

    def dfs_cicle(self, graph, vertex, visited, dad):
        # Marca o vértice atual como visitado
        visited.add(vertex)

        # Itera sobre cada vértice adjacente ao vértice atual
        for adjacent in graph[vertex]:
            # Se o adjacente não foi visitado, faz uma DFS a partir dele
            if adjacent not in visited:
                if self.dfs_cicle(graph, adjacent, visited, vertex):
                    return True
            # Se o adjacente foi visitado e não é o pai do vértice atual, encontramos um ciclo
            elif adjacent != dad:
                return True

        return False

    def has_cicle(self):
        visited = set()
        # Chama a função dfs_ciclo para cada vértice não visitado
        for vertex in self.graph:
            if vertex not in visited:
                if self.dfs_cicle(self.graph, vertex, visited, None):
                    return True
        return False

    def display(self):
        print(self.graph)
        for i in self.graph.values():
            print(i)


# Exemplo de uso
g = Graph()

g.add_edge(0, 1)
g.add_edge(2, 0)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("\nVerificação se o grafo tem ciclo:")
print("O grafo tem ciclo") if g.has_cicle() else print("O grafo não tem clico")
