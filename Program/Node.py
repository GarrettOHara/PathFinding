import math
class Node:
    def __init__(self, x, y, nodeType):
        self.xPos = x
        self.yPos = y
        self.nodeType = nodeType

    #f = g + h
    #function that calculates h
    #"h" is the heuristic (estimated distance between the current node and the end node)
    def findHeuristic(self, endNode):
        x1 = self.xPos
        x2 = endNode.xPos
        y1 = self.yPos
        y2 = endNode.yPos
        xDifference = x2 - x1
        yDifference = y2 - y1
        return math.sqrt((int(math.pow(xDifference, 2))) + (int(math.pow(yDifference, 2))))
        #alternative calculation: self.heuristic = math.sqrt(((endNode.xPos - self.xPos)**2) - ((endNode.yPos - self.yPos)**2))

    #function that calculates g
    #"g" is the distance between the current node and the start node
    def findCurrentCost(self, startNode):
        return 0

    #function that calculates f
    #"f" is the total cost
    def findTotalCost(self, start, end):
        return (self.findCurrentCost(start) + self.findHeuristic(end))
