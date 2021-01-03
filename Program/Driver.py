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
    newGraph = Graph(size, startX, startY, endX, endY)
    newGraph.populate()

    #start the a star algorithm
    algorithm = AStarAlgorithm(newGraph)
    algorithm.startAlgorithm()