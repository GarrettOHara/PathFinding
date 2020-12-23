import math
class Node:

    nodeType = "" #4 types of nodes: start, end, obstacle, open

    heuristic = 0 # the heuristic (estimated distance between the current node and the end node)
    currentCost = 0 # the distance between the current node and the start node

    xPos = 0 #the x position of the node on the graph
    yPos = 0 #the y position of the node on the graph

    def __init__(self, x, y, nodeType):
        self.xPos = x
        self.yPos = y
        self.nodeType = nodeType

    #f = g + h
    #function that calculates the heuristic (h)
    def findHeuristic(self, endNode):
        x1 = self.xPos
        x2 = endNode.xPos
        y1 = self.yPos
        y2 = endNode.yPos
        xDifference = x2 - x1
        yDifference = y2 - y1
        self.heuristic = math.sqrt((int(math.pow(xDifference, 2))) + (int(math.pow(yDifference, 2))))
        #self.heuristic = math.sqrt((endNode.xPos - currNode.xPos)**2 - (endNode.yPos - currNode.yPos)**2)

    #function that calculates currentCost (g) (distance from current node to start node)
    def findCurrentCost(self, startNode, currentNode):
        print("Hello")
    