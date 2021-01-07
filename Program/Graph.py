from Node import Node
import math
class Graph:
    def __init__(self,size,startX,startY,endX,endY):
        self.graph = [[Node(x,y,"open") for x in range(size)] for y in range(size)]
        self.graph[startX][startY].nodeType = "start"
        self.graph[endX][endY].nodeType = "end"
        self.startNode = self.graph[startX][startY]
        self.endNode = self.graph[endX][endY]
    
    def displayGraph(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                print(self.graph[x][y])
            print("")
        print(self.startNode)
        print(self.endNode)
    
    def getAdj(self, node):
        adjNodes = []
        x = int(node.xPos)
        y = int(node.yPos)
        if(self.inRange(x,y+1)):
            adjNodes.append(self.graph[x][y+1])
        if(self.inRange(x+1,y+1)):
            adjNodes.append(self.graph[x+1][y+1])
        if(self.inRange(x+1,y)):
            adjNodes.append(self.graph[x+1][y])
        if(self.inRange(x+1,y-1)):
            adjNodes.append(self.graph[x+1][y-1])
        if(self.inRange(x,y-1)):
            adjNodes.append(self.graph[x][y-1])
        if(self.inRange(x-1,y-1)):
            adjNodes.append(self.graph[x-1][y-1])
        if(self.inRange(x-1,y)):
            adjNodes.append(self.graph[x-1][y])
        if(self.inRange(x-1,y+1)):
            adjNodes.append(self.graph[x-1][y+1])
        return adjNodes

    
    def inRange(self, x, y):
        if(x in range(len(self.graph) and y in range(len(self.graph[0])))):
            return True
        else:
            return False
    
    def findShortestPath(self):
        openList = []
        closedList = []

        openList.append(self.startNode)

        while(len(openList) > 0):

            minNode = openList[0]
            minIndex = 0
            for i in range(len(openList)):
                if(minNode.f < openList[i].f):
                    minNode = openList[i]
                    minIndex = i
            
            openList.pop(minIndex)
            print(minIndex)
            closedList.append(minNode)
            print(minNode)

            if(minNode == self.endNode):
                print(*closedList)
                return closedList
            
            adjNodes = self.getAdj(minNode)

            print(len(adjNodes))

            for node in adjNodes:
                
                for closedNode in closedList:
                    if(node == closedNode):
                        continue

                node.g = minNode.g + 1
                node.h = math.sqrt(((self.endNode.xPos - node.xPos)**2) + ((self.endNode.yPos - node.yPos)**2))
                node.f = node.h + node.g

                for openNode in openList:
                    if(node == openNode and node.g > openNode.g):
                        continue
                
                openList.append(node)