from tkinter import *
from Node import Node
import math

class Graph:
    def __init__(self,master,size,startX,startY,endX,endY):
        self.graph = [[Node(x,y,"open") for y in range(size)] for x in range(size)]
        self.graph[startX][startY].nodeType = "start"
        self.graph[endX][endY].nodeType = "end"
        self.startNode = self.graph[startX][startY]
        self.endNode = self.graph[endX][endY]
        self.graph[5][5].nodeType = "closed"

        self.displayGraph()

        findPathBtn = Button(window, text="Find Path")
        findPathBtn.bind("<Button-1>", self.findShortestPath)
        #place location fo the button here

    
    
    def displayGraph(self):
        """for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                print(self.graph[x][y]),
            print("")"""
        for x in range(len(self.graph)):
            for y in range(len(self.grah[0])):
                if self.graph[x][y].nodeType == 'open':
                    frame = tk.Frame(
                        master=window,
                        bg='white',
                        relief=tk.RAISED,
                        borderwidth=1
                    )
                    frame.grid(row=x,column=y)
                elif self.graph[x][y].nodeType == 'start':
                    frame = tk.Frame(
                        master=window,
                        bg='green',
                        relief=tk.RAISED,
                        borderwidth=1
                    )
                elif self.graph[x][y].nodeType == 'end':
                    frame = tk.Frame(
                        master=window,
                        bg='red',
                        relief=tk.RAISED,
                        borderwidth=1
                    )

    """
    What we still need to do:
        - Get the graph displayed on the tkinter window
        - Create command line arguments for the metaData of the graph obj
        - Write an event handler that changes the nodes from open to closed on <Button-1>
        - Troubleshoot our messups
    """
                


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
    
    def findShortestPath(self):
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

window = Tk()
w = Graph(window)
window.geometry('1000x1000')
window.title('Tkinter Testing')
window.mainloop()