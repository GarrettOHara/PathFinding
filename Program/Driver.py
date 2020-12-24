from Node import Node
class Driver:
    #graph size
    size = 15
    graph = [size][size]

    #populate graph with empty nodes
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            node = Node(x,y,"open")

    #start and end node
    startNode = Node(5,5,"start")
    graph[5][5] = startNode

    endNode = Node(10,10,"end")
    graph[10][10] = endNode