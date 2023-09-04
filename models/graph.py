
class Graph:
    def __init__(self, amount_nodes):
        self.nodes = amount_nodes
        self.graph = [[] for i in range(self.nodes)]

    def print_graph(self):
        for i in range(self.nodes):
            print(f'{i + 1}:', end='  ')
            for j in self.graph[i]:
                print(f'{j} ->', end='  ')
            print('')

    def create_edge(self, start, end, distance):
        self.graph[start - 1].append([end, distance])
        self.graph[end - 1].append([start, distance])


g = Graph(4)

g.create_edge(1, 2, 9)
g.create_edge(2, 3, 5)
g.create_edge(1, 4, 7)



g.print_graph()
