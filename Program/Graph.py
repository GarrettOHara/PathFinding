from Node import Node
class Graph:
    def __init__(self, size, startX, startY, endX, endY):
        graphSize = int(size)
        self.graph = [graphSize][graphSize]
        self.startNode = Node(startX,startY,"start")
        self.endNode = Node(endX,endY,"end")

    def populate(self):
        self.startNode.setStartNode(self.startNode)
        self.endNode.setEndNode(self.endNode)
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                if((x == (self.startNode.xPos) and y == (self.startNode.yPos)) or \
                   (x == (self.endNode.xPos) and y == (self.endNode.yPos))):
                   #account for closed nodes
                   continue
                else:
                    self.graph[x][y] = Node(x,y,"open")
                    self.graph[x][y].setStartNode(self.startNode)
                    self.graph[x][y].setEndNode(self.endNode)
    
    def clear(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                if((self.graph[x][y].nodeType == "start") or \
                   (self.graph[x][y].nodeType == "end")   or \
                   (self.graph[x][y].nodeType == "closed")):
                    self.graph[x][y].nodeType = "open"