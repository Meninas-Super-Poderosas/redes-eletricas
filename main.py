from edges import Edge
from graph import Graph
from nodes import Node


def main():
    main_graph = Graph()
    try:
        first_answer = input("Do you want to create the graph yourself? (y to YES or any key to NO) ")
        if first_answer.lower() != 'y':
            print('All right, we will create a graph for you...')

            node1 = Node("DC", 1239)
            node2 = Node("Ceagri I", 1100)
            node3 = Node("Cegoe", 4900)
            node4 = Node("DB", 700)
            node5 = Node("Depaq", 200)
            node6 = Node("Reitoria", 212)

            main_graph.create_node(node1)
            main_graph.create_node(node2)
            main_graph.create_node(node3)
            main_graph.create_node(node4)
            main_graph.create_node(node5)
            main_graph.create_node(node6)

            edge1 = Edge(node1, node2, 15)
            edge2 = Edge(node2, node3, 13)
            edge3 = Edge(node1, node3, 20)
            edge4 = Edge(node3, node5, 5)
            edge5 = Edge(node5, node4, 8)
            edge6 = Edge(node2, node4, 5)
            edge7 = Edge(node4, node6, 15)
            edge8 = Edge(node2, node6, 25)
            edge9 = Edge(node6, node5, 21)
            edge10 = Edge(node3, node4, 10)

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

        elif first_answer.lower() == "y":
            amount_nodes = int(input("How many nodes do you want in the graph? "))

            print('')
            print("All right, now specify the Departments (Nodes): ")
            print('')

            for i in range(amount_nodes):
                name = input(f'Department {i + 1} name: ')
                amount_people = int(input(f'Department {i + 1} people: '))
                new_node = Node(name, amount_people)
                main_graph.create_node(new_node)

            print(f'All right, now, specify the edges: ')
            print(f"Be careful, don't create identical edges!")
            print('')

            while True:
                start = input("Start department name: ")
                final = input("Final Department name: ")
                distance = input("Distance between them: ")

                node_start = None
                node_final = None

                for nodes in main_graph.nodes:
                    if start == nodes.department_name:
                        node_start = nodes
                for nodes in main_graph.nodes:
                    if final == nodes.department_name:
                        node_final = nodes

                if node_start is not None and node_final is not None:
                    created_edge = Edge(node_start, node_final, distance)
                    main_graph.create_edge(created_edge)
                else:
                    print("Invalid department names. Please try again.")

                conf = input('Do you want to create any connections? (y/n) ')
                if conf != "y":
                    break

        print('')

        print("All right, here is your graph:")

        print('')

        main_graph.print_graph(main_graph)

        print('')

        second_answer = input("Do you want to remove any edge that has been created? (y/no) ")
        while second_answer != 'no':
            if second_answer == 'y':
                print('')
                print(
                    "All right! You chose to remove an edge."
                    " Now, specify the nodes of the edge that you want to remove: ")
                start_dept_name = input("Start Department: ")
                end_dept_name = input("End Department: ")
                target = main_graph.find_edge(start_dept_name, end_dept_name)
                if target is not None:
                    main_graph.delete_edge(main_graph.edges, target)
                    print("Success!")
                    print('')
                else:
                    print("Sorry, this edge doesn't exist in your graph")
                    print('')
            elif second_answer != 'y':
                print("Oh, seems like you typed the wrong key, let's try again")
                print('')
            print("Here is your modified graph:")
            main_graph.print_graph(main_graph)
            print('')
            second_answer = input("Do you want to remove any edge that you have been created? (y/no) ")

        minimum_spanning_tree = main_graph.kruskal()

        print("Here is your Minimal Spanning Tree:")

        print('')

        main_graph.print_mst(minimum_spanning_tree)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
