from Node import Node
from Graph import Graph
from AStarAlgorithm import AStarAlgorithm
class Driver:
    #initializing the graph
    size = 15
    graph = [size][size]

    #populating the graph with open nodes (empty nodes)
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            node = Node(x,y,"open")

    #manually setting the start node and end node
    startX = 5
    startY = 5
    startNode = Node(startX,startY,"start")
    graph[startX][startY] = startNode

    endX = 10
    endY = 10
    endNode = Node(endX,endY,"end")
    graph[endX][endY] = endNode

    newGraph = Graph(graph)
    newGraph.setStartNode(startNode)
    newGraph.setEndNode(endNode)

    algorithm = AStarAlgorithm()
    algorithm.addStartNode(startNode)