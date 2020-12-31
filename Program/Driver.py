from Node import Node
from Graph import Graph
from AStarAlgorithm import AStarAlgorithm
class Driver:
    print("Enter the size of the graph: ")
    size = input()
    print("Enter the x value of the start node: ")
    startX = input()
    print("Enter the y value of the start node: ")
    startY = input()
    print("Enter the x value of the end node: ")
    endX = input()
    print("Enter the y value of the end node: ")
    endY = input()

    #initializing the graph
    newGraph = Graph(size, startX, startY, endX, endY)
    newGraph.populate()

    #start the a star algorithm
    algorithm = AStarAlgorithm(newGraph)
    algorithm.startAlgorithm()