from edges import Edge
from graph import Graph
from nodes import Node

# amount_nodes = int(input("How much nodes do you want in graph? "))
#
# # Graph creation with specified quantity of nodes (departments) in context of this application.
# main_graph = Graph()
#
# print('')
# print("All right, now specify the Departments (Nodes): ")
# print('')
#
# for i in range(amount_nodes):
#     name = input(f'department {i+1} name: ')
#     amount_people = int(input(f'department {i + 1} peoples: '))
#     new_node = Node(name, amount_people)
#     main_graph.create_node(new_node)
#
# print(f'All right, now, specify the edges. max{amount_nodes - 1}')
#
# while True:
#     start = input("Start department name: ")
#     final = input("Final Department name: ")
#     distance = input("Distance between them: ")
#
#     node_start = 1
#     node_final = 1
#
#     for nodes in main_graph.nodes:
#         if start == nodes.department_name:
#             node_start = nodes
#     for nodes in main_graph.nodes:
#         if final == nodes.department_name:
#             node_final = nodes
#
#     created_edge = Edge(node_start, node_final, distance)
#     main_graph.create_edge(created_edge)
#
#     conf = input('Do you want to create any connections? (y/n) ')
#     if conf != "y":
#         break
#
# print("")
# main_graph.print_graph()

main_graph = Graph()

node1 = Node("DC", 3000)
node2 = Node("Ceagri I", 200)
node3 = Node("Cegoe", 2500)
node4 = Node("DB", 100)
node5 = Node("Depaq", 200)
node6 = Node("Reitoria", 2)

main_graph.create_node(node1)
main_graph.create_node(node2)
main_graph.create_node(node3)
main_graph.create_node(node4)
main_graph.create_node(node5)
main_graph.create_node(node6)

# edge1 = Edge(node1, node2, 15)
# edge2 = Edge(node2, node3, 13)
# edge3 = Edge(node1, node3, 20)
# edge4 = Edge(node3, node5, 5)
# edge5 = Edge(node5, node4, 8)
# edge6 = Edge(node2, node4, 5)
# edge7 = Edge(node4, node6, 15)
# edge8 = Edge(node2, node6, 25)
# edge9 = Edge(node6, node5, 21)
# edge10 = Edge(node3, node4, 10)

edge4 = Edge(node3, node5, 5)
edge6 = Edge(node2, node4, 5)
edge5 = Edge(node5, node4, 8)
edge10 = Edge(node3, node4, 10)
edge2 = Edge(node2, node3, 13)
edge1 = Edge(node1, node2, 15)
edge7 = Edge(node4, node6, 15)
edge3 = Edge(node1, node3, 20)
edge9 = Edge(node6, node5, 21)
edge8 = Edge(node2, node6, 25)


main_graph.create_edge(edge1)
main_graph.create_edge(edge2)
main_graph.create_edge(edge3)
main_graph.create_edge(edge4)
main_graph.create_edge(edge5)
main_graph.create_edge(edge6)
main_graph.create_edge(edge7)
main_graph.create_edge(edge8)
main_graph.create_edge(edge9)
main_graph.create_edge(edge10)

minimum_spanning_tree = main_graph.kruskal()
for edge in minimum_spanning_tree:
    print(f"{edge.start.department_name} -> {edge.end.department_name} cost: {edge.distance}")

