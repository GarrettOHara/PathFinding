from Node import Node
from Graph import Graph
from AStarAlgorithm import AStarAlgorithm
class Driver:

    size = input("Enter the size of the graph: ")
    startX = input("Enter the x value of the start node: ")
    startY = input("Enter the y value of the start node: ")
    endX = input("Enter the x value of the end node: ")
    endY = input("Enter the y value of the end node: ")

    #initializing the graph
    newGraph = Graph(size)
    newGraph.populate(startX, startY, endX, endY)

    #populating the graph
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if(x == startX and y == startY):
                graph[x][y] = Node(x,y,"start")
            else if(x == endX and y == endY):
                graph[x][y] = Node(x,y,"end")
            else:
                graph[x][y] = Node(x,y,"open")

    algorithm = AStarAlgorithm(newGraph)
    algorithm.startAlgorithm()