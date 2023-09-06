class Node:
    def __init__(self, department_name, amount):
        self.department_name = department_name
        self.person_qtd = amount
        self.edge = []

    def add_edge(self, edge):
        self.edge.append(edge)
