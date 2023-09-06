from nodes import Node
from edges import Edge


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def create_node(self, node):
        self.nodes.append(node)

    def create_edge(self, edge):
        self.edges.append(edge)

    def print_graph(self):
        printed_edges = set()
        for i in self.nodes:
            print(f'{i.department_name}:', end='     ')
            for edge in self.edges:
                if edge.start == i:
                    if (edge.start, edge.end) not in printed_edges:
                        print(f'{edge.start.department_name} -> {edge.end.department_name} cost: ({edge.distance})', end='    ')
                        printed_edges.add((edge.start, edge.end))
                elif edge.end == i and (edge.end, edge.start) not in printed_edges:
                    print(f'{edge.end.department_name} -> {edge.start.department_name} cost: ({edge.distance})', end='    ')
                    printed_edges.add((edge.end, edge.start))
            print('')
