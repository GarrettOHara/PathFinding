import math
class Node:
    #each Node has one of four types: open, obstacle, start, end
    nodeType = "none"
    #the x position of the Node on the graph
    xPos = -1
    #the y position of the Node on the graph
    yPos = -1

    #f = g + h
    #"h" the heuristic (estimated distance between the current node and the end node)
    heuristic = -1
    #"g" the distance between the current node and the start node
    currentCost = -1
    #"f" the total cost
    totalCost = -1

    def __init__(self, x, y, nodeType):
        self.xPos = x
        self.yPos = y
        self.nodeType = nodeType

    #function that calculates h
    def findHeuristic(self, endNode):
        x1 = self.xPos
        x2 = endNode.xPos
        y1 = self.yPos
        y2 = endNode.yPos
        xDifference = x2 - x1
        yDifference = y2 - y1
        self.heuristic = math.sqrt((int(math.pow(xDifference, 2))) + (int(math.pow(yDifference, 2))))
        #alternative calculation: self.heuristic = math.sqrt(((endNode.xPos - self.xPos)**2) - ((endNode.yPos - self.yPos)**2))

    #function that calculates g
    def findCurrentCost(self, startNode):
        self.currentCost = 0

    #function that calculates f
    def findTotalCost(self):
        self.totalCost = self.currentCost + self.heuristic
