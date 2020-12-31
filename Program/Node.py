import math
class Node:

    def __init__(self, x, y, nodeType):
        self.xPos = x
        self.yPos = y
        self.nodeType = nodeType
        self.heuristic = -1
        self.currentCost = -1
        self.totalCost = -1
        self.startNode = Node(-1, -1, "none")
        self.endNode = Node(-1, -1, "none")
    
    def setStartNode(self, node):
        self.startNode.xPos = node.xPos
        self.startNode.yPos = node.yPos
        self.startNode.nodeType = node.nodeType
    
    def getStartNode(self):
        return self.startNode
    
    def setEndNode(self, node):
        self.endNode.xPos = node.xPos
        self.endNode.yPos = node.yPos
        self.endNode.nodeType = node.nodeType
    
    def getEndNode(self):
        return self.endNode

    #f = g + h
    #function that calculates h
    #"h" is the heuristic (estimated distance between the current node and the end node)
    def findHeuristic(self):
        x1 = self.xPos
        x2 = self.endNode.xPos
        y1 = self.yPos
        y2 = self.endNode.yPos
        xDifference = x2 - x1
        yDifference = y2 - y1
        self.heuristic = math.sqrt((int(math.pow(xDifference, 2))) + (int(math.pow(yDifference, 2))))
        #alternative calculation: self.heuristic = math.sqrt(((endNode.xPos - self.xPos)**2) - ((endNode.yPos - self.yPos)**2))

    #function that calculates g
    #"g" is the distance between the current node and the start node
    def findCurrentCost(self):
        return 0

    #function that calculates f
    #"f" is the total cost
    def findTotalCost(self):
        return (self.findCurrentCost() + self.findHeuristic())

    def __lt__(self, other):
        return self.totalCost < other.totalCost
