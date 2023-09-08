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

    def find_edge(self, edge_list, start, end):
        for edge in edge_list:
            if edge.start is start and edge.end is end:
                return edge
        return None

    def delete_edge(self, edge_list, target):
        if target in edge_list:
            edge_list.remove(edge_list)
        else:
            print("that edge doesn't exist.")

    def find_root(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_root(parent, parent[node])

    def join(self, parent, rank, u, v):
        lord_a = self.find_root(parent, u)
        lord_b = self.find_root(parent, v)
        if lord_a != lord_b:
            if rank[lord_a] < rank[lord_b]:
                parent[lord_a] = lord_b
            elif rank[lord_a] > rank[lord_b]:
                parent[lord_b] = lord_a
            else:
                parent[lord_b] = lord_a
                rank[lord_a] += 1

    def kruskal(self):
        mst_edges = []
        self.edges.sort(key=lambda edge: edge.distance)

        parent = {node: node for node in self.nodes}
        rank = {node: 0 for node in self.nodes}

        for edge in self.edges:
            u, v = edge.start, edge.end
            if self.find_root(parent, u) != self.find_root(parent, v):
                mst_edges.append(edge)
                self.join(parent, rank, u, v)

        return mst_edges

    def print_graph(self, graph):
        printed_edges = set()
        for i in graph.nodes:
            print(f'{i.department_name}:', end='     ')
            for edge in graph.edges:
                if edge.start == i:
                    if (edge.start, edge.end) not in printed_edges:
                        print(f'{edge.start.department_name} -> {edge.end.department_name} cost: ({edge.distance})',
                              end='    ')
                        printed_edges.add((edge.start, edge.end))
                elif edge.end == i and (edge.end, edge.start) not in printed_edges:
                    print(f'{edge.end.department_name} -> {edge.start.department_name} cost: ({edge.distance})',
                          end='    ')
                    printed_edges.add((edge.end, edge.start))
            print('')

    def print_mst(self, mst):
        for edge in mst:
            print(f"{edge.start.department_name} -> {edge.end.department_name} cost: {edge.distance}")