import tkinter as tk
#from Node import Node
import math
import sys

class Node:
    OPEN = "white"
    CLOSED = "gray" #or black
    FINAL_PATH = "red"
    OPEN_CLOSED = "green"

    def __init__(self,x,y,nodeType):
        self.xPos = int(x)
        self.yPos = int(y)
        self.nodeType = str(nodeType)
        self.size = 50

        self.h = 0
        self.g = 0
        self.f = 0
    
    def __eq__(self,node):
        if((self.xPos == node.xPos) and (self.yPos == node.yPos)):
            return True
        else:
            return False
    
    def __str__(self):
        return ("(" + str(self.xPos) + "," + str(self.yPos) 
            + "," + self.nodeType + ")")
    
    def _switch(self):
        print("Null")
        #switch the node color based on keybaord input
    
    def printType(self):
        print("Null")        

    def draw(self, x, y):
        if self.nodeType == 'open':
            frame = tk.Frame(
                master=window,
                bg="black",
                borderwidth=1,
                width = 40,
                height = 40
            )
            frame.grid(row=x,column=y)
            label = tk.Label(master = frame, text="     ")
            label.pack()
        elif self.nodeType == 'start':
            frame = tk.Frame(
                master=window,
                borderwidth=1,
                width = 40,
                height = 40
            )
            frame.grid(row=x,column=y)
            label = tk.Label(master = frame, bg="green", text="     ")
            label.pack()
        elif self.nodeType == 'end':
            frame = tk.Frame(
                master=window,
                borderwidth=1,
                width = 40,
                height = 40
            )
            frame.grid(row=x,column=y)
            label = tk.Label(master = frame, bg="red", text="     ")
            label.pack()


class Graph:
    def __init__(self,master,size,startX,startY,endX,endY):
        self.cellSize = 50
        self.graph = [[Node(x,y,"open") for y in range(size)] for x in range(size)]
        self.graph[startX][startY].nodeType = "start"
        self.graph[endX][endY].nodeType = "end"
        self.startNode = self.graph[startX][startY]
        self.endNode = self.graph[endX][endY]
        self.graph[5][5].nodeType = "closed"

        self.displayGraph()

        findPathBtn = tk.Button(window, text="Find Path")
        findPathBtn.bind("<Button-1>", self.findShortestPath)
        findPathBtn.grid(row=size+1,column=size+1)

        #printBtn = tk.Button(window, text="Test")
        window.bind("<Button-1>", self.handleMouseClick)
        #printBtn.grid(row=size+2,column=size+1)

    def printSomething(self, event):
        print()
    
    def _eventCoords(self, event):
        row = int(event.y)
        col = int(event.x)
        print(row), 
        print(col)
        return row, col

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        self.graph[row][column].nodeType = "closed"
        self.drawObsticle(row, column)
    
    def drawObsticle(self, row, col):
        frame = tk.Frame(
                master=window,
                bg="black",
                borderwidth=1,
                width = 40,
                height = 40
            )
        frame.grid(row=row,column=col)
        label = tk.Label(master = frame, bg = "gray", text="     ")
        label.pack()

    def displayGraph(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[0])):
                self.graph[x][y].draw(x, y)

    def pathButton(self, event):
        self.findShortestPath

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
            print(node),
        print("")

        return adjNodes

    
    def inRange(self,x,y):
        if(((x > -1) and (x < len(self.graph))) and ((y > - 1) and (y < len(self.graph)))):
            return True
        else:
            return False
    
    def findShortestPath(self, event):
        openList = []
        closedList = []

        openList.append(self.startNode)
        count = 0

        while(len(openList) > 0):

            minNode = openList[0]
            minIndex = 0
            for i in range(len(openList)):
                if(minNode.f > openList[i].f):
                    minNode = openList[i]
                    minIndex = i
            
            openList.pop(minIndex)
            closedList.append(minNode)

            if(minNode == self.endNode):
                print("Found the end node")
                
                for item in closedList:
                    print(item)
                return
                    

            adjNodes = self.getAdj(minNode)

            for node in adjNodes:
                if node.nodeType == "closed":
                    continue

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

size = int(sys.argv[1])
startX = int(sys.argv[2])
startY = int(sys.argv[3])
endX = int(sys.argv[4])
endY = int(sys.argv[5])

window = tk.Tk()
w = Graph(window, size, startX, startY, endX, endY)
#window.geometry('1000x1000')
window.title('Path Finder')
window.mainloop()

"""
What we still need to do:
    X- Get the graph displayed on the tkinter window
    X- Create command line arguments for the metaData of the graph obj
    - Address the thread issue in Tkinter when running the path fuction
    - Write an event handler that changes the nodes from open to closed on <Button-1>
    - Troubleshoot our messups
"""