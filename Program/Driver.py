from Node import Node
from Graph import Graph
class Driver:
    size = int(input("Enter the size of the graph: "))
    startX = int(input("Enter the x value of the start node: "))
    startY = int(input("Enter the y value of the start node: "))
    endX = int(input("Enter the x value of the end node: "))
    endY = int(input("Enter the y value of the end node: "))

    graph = Graph(size,startX,startY,endX,endY)
    graph.displayGraph()
    graph.findShortestPath()