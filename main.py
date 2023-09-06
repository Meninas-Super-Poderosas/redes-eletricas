from edges import Edge
from graph import Graph
from nodes import Node

amount_nodes = int(input("How much nodes do you want in graph? "))

# Graph creation with specified quantity of nodes (departments) in context of this application.
main_graph = Graph()

print('')
print("All right, now specify the Departments (Nodes): ")
print('')

for i in range(amount_nodes):
    name = input(f'department {i+1} name: ')
    amount_people = int(input(f'department {i + 1} peoples: '))
    new_node = Node(name, amount_people)
    main_graph.create_node(new_node)

print(f'All right, now, specify the edges. max{amount_nodes - 1}')

while True:
    start = input("Start department name: ")
    final = input("Final Department name: ")
    distance = input("Distance between them: ")

    node_start = 1
    node_final = 1

    for nodes in main_graph.nodes:
        if start == nodes.department_name:
            node_start = nodes
    for nodes in main_graph.nodes:
        if final == nodes.department_name:
            node_final = nodes

    created_edge = Edge(node_start, node_final, distance)
    main_graph.create_edge(created_edge)

    conf = input('Do you want to create any connections? (y/n) ')
    if conf != "y":
        break

print("")
main_graph.print_graph()
