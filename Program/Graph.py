from Node import Node
class Graph:

    def __init__(self, size):
        self.graph = [size][size]
        self.startNode = Node(-1,-1,"none")
        self.endNode = Node(-1,-1,"none")

    def populate(self, startX, startY, endX, endY):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                if(x == startX and y == startY):
                    self.graph[x][y] = Node(x,y,"start")
                elif(x == endX and y == endY):
                    self.graph[x][y] = Node(x,y,"end")
                else:
                    self.graph[x][y] = Node(x,y,"open")
    
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
    
    def clear(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                if((self.graph[x][y].nodeType == "start") or \
                   (self.graph[x][y].nodeType == "end")   or \
                   (self.graph[x][y].nodeType == "closed")):
                    self.graph[x][y].nodeType = "open"