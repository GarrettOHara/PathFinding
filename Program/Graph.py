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
        print(" ")
        nodes = []
        nodeX = int(node.xPos)
        nodeY = int(node.yPos)
        nodes.append(self.get((nodeX), (nodeY + 1)))
        nodes.append(self.get((nodeX + 1), (nodeY + 1)))
        nodes.append(self.get((nodeX + 1), (nodeY)))
        nodes.append(self.get((nodeX + 1), (nodeY - 1)))
        nodes.append(self.get((nodeX), (nodeY - 1)))
        nodes.append(self.get((nodeX - 1), (nodeY - 1)))
        nodes.append(self.get((nodeX - 1), (nodeY)))
        nodes.append(self.get((nodeX - 1), (nodeY + 1)))
        return nodes
    
    def get(self, x, y):
        if(((x in range(len(self.graph))) and (y in range(len(self.graph[0]))))):
            return self.graph[x][y]
        else:
            temp = Node(-1,-1,"closed")
            return temp
    
    def clear(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                if((self.graph[x][y].nodeType == "start") or \
                   (self.graph[x][y].nodeType == "end")   or \
                   (self.graph[x][y].nodeType == "closed")):
                    self.graph[x][y].nodeType = "open"