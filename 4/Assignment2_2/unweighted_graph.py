class UnweightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

unweighted_graph = UnweightedGraph()
unweighted_graph.add_vertex("A")
unweighted_graph.add_vertex("B")
unweighted_graph.add_vertex("C")
unweighted_graph.add_edge("A", "B")
unweighted_graph.add_edge("A", "C")
unweighted_graph.add_edge("B", "C")

unweighted_graph.print_graph()

