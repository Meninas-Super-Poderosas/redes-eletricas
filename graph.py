from edges import Edge


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def create_node(self, node):
        self.nodes.append(node)

    def create_edge(self, edge):
        self.edges.append(edge)
        aux_edge = Edge(edge.end, edge.start, edge.distance)
        self.edges.append(aux_edge)

    def find_edge(self, start, end):
        for edge in self.edges:
            if edge.start.department_name.lower() == start.lower() and edge.end.department_name.lower() == end.lower():
                return edge
        return None

    def delete_edge(self, edge_list, target):
        reverse_edge = Edge(target.end, target.start, target.distance)

        found_target = None
        found_reverse_edge = None

        for edge in edge_list:
            if edge.start == target.start and edge.end == target.end and edge.distance == target.distance:
                found_target = edge
            if (edge.start == reverse_edge.start and
                    edge.end == reverse_edge.end and
                    edge.distance == reverse_edge.distance):
                found_reverse_edge = edge

        if found_target is not None and found_reverse_edge is not None:
            edge_list.remove(found_target)
            edge_list.remove(found_reverse_edge)
        else:
            print("The edge doesn't exist.")

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
        nodes_aux = []
        km = 0
        people = 0
        cost_per_kilometer = 1782

        for edge in mst:

            print(f"{edge.start.department_name} -> {edge.end.department_name} cost: {edge.distance}")

            km += edge.distance

            if edge.start not in nodes_aux:
                nodes_aux.append(edge.start)

            if edge.end not in nodes_aux:
                nodes_aux.append(edge.end)
        for node in nodes_aux:
            people += int(node.person_qtd)

        print('')

        print(f"this project used up {km * cost_per_kilometer} dollars and helped out {people} people")
