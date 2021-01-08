from Node import Node
import math
class Graph:
    def __init__(self,size,startX,startY,endX,endY):
        self.graph = [[Node(x,y,"open") for y in range(size)] for x in range(size)]
        self.graph[startX][startY].nodeType = "start"
        self.graph[endX][endY].nodeType = "end"
        self.startNode = self.graph[startX][startY]
        self.endNode = self.graph[endX][endY]
    
    def displayGraph(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                print(self.graph[x][y],end=" ")
            print("")
    
    def getAdj(self,node):
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
        
        for node in adjNodes:
            print(node,end=" ")
        print("")

        return adjNodes

    
    def inRange(self,x,y):
        if(((x > -1) and (x < len(self.graph))) and ((y > - 1) and (y < len(self.graph)))):
            return True
        else:
            return False
    
    def findShortestPath(self):
        openList = []
        closedList = []

        openList.append(self.startNode)
        count = 0

        while(len(openList) > 0 and count < 20):

            count = count + 1

            minNode = openList[0]
            minIndex = 0
            for i in range(len(openList)):
                if(minNode.f < openList[i].f):
                    minNode = openList[i]
                    minIndex = i
            
            openList.pop(minIndex)
            closedList.append(minNode)

            if(minNode == self.endNode):
<<<<<<< HEAD
                path = []
                current = minNode
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path
            #return closedList
=======
                return closedList
>>>>>>> 70c3027bca9d45f397626a0278a87c40304526e5
            
            adjNodes = self.getAdj(minNode)

            for node in adjNodes:
                
                for closedNode in closedList:
                    if(node == closedNode):
                        continue

                node.g = minNode.g + 1
                node.h = ((node.xPos - self.endNode.xPos)**2) + ((node.yPos - self.endNode.yPos)**2)
                node.f = node.h + node.g

                for openNode in openList:
                    if((node == openNode) and (node.g > openNode.g)):
                        continue
                
                openList.append(node)