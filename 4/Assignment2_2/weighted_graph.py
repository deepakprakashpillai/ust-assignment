class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, weight))
            self.adjacency_list[vertex2].append((vertex1, weight))

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

weighted_graph = WeightedGraph()
weighted_graph.add_vertex("A")
weighted_graph.add_vertex("B")
weighted_graph.add_vertex("C")
weighted_graph.add_edge("A", "B", 5)
weighted_graph.add_edge("A", "C", 10)
weighted_graph.add_edge("B", "C", 15)

weighted_graph.print_graph()
