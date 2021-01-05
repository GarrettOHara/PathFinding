from Node import Node
class Graph:
    def __init__(self, size, startX, startY, endX, endY):
        size = int(size)
        self.graph = [[Node(-1, -1, "none") for y in range(size)] for x in range(size)]
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
    
    def getAdjacentNodes(self, node):
        print("")
        nodes = []
        nodes.append(self.get((node.xPos), (node.yPos + 1)))
        nodes.append(self.get((node.xPos + 1), (node.yPos + 1)))
        nodes.append(self.get((node.xPos + 1), (node.yPos)))
        nodes.append(self.get((node.xPos + 1), (node.yPos - 1)))
        nodes.append(self.get((node.xPos), (node.yPos - 1)))
        nodes.append(self.get((node.xPos - 1), (node.yPos - 1)))
        nodes.append(self.get((node.xPos - 1), (node.yPos)))
        nodes.append(self.get((node.xPos - 1), (node.yPos + 1)))
        return nodes
    
    def get(self, x, y):
        print("")
        return self.graph[x][y]
    
    def clear(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                if((self.graph[x][y].nodeType == "start") or \
                   (self.graph[x][y].nodeType == "end")   or \
                   (self.graph[x][y].nodeType == "closed")):
                    self.graph[x][y].nodeType = "open"