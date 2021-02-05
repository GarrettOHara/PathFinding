import tkinter as tk
import sys

class Node:
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

class NodeGUI(tk.Frame):
    BLOCK_COLOR = "black"
    CLEAR_COLOR = "white"
    GROWTH_COLOR= "blue"
    PATH_COLOR  = "red"
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(borderwidth=1, bg=self.CLEAR_COLOR, relief=tk.RAISED)
        self.bind('<B1-Motion>', self.on_click)
        self.bind('<1>', self.on_click)
        self.bind('<2>', self.on_DeleteClick)

    def on_click(self, event=None):
        self['bg'] = self.BLOCK_COLOR
        print(self.graph[1][1].nodeType)
        """
        This will switch on and off

        if self['bg'] == self.CLEAR_COLOR:
            self['bg'] = self.BLOCK_COLOR
        else:
            self['bg'] = self.CLEAR_COLOR
        """
    def on_DeleteClick(self,event=None):
        self['bg'] = self.CLEAR_COLOR

class GraphGUI(tk.Frame):
    def __init__(self,master=None, rows = 20, columns = 20,
        size=20,startX=2,startY=2,endX=15,endY=15,**kwargs):
        super().__init__(master, **kwargs)
        G = Graph(master,20,2,2,15,15)
        for row_num in range(rows):
            for col_num in range(columns):
                f = NodeGUI(self)
                f.grid(row=row_num, column=col_num, sticky='nsew')
        self.rowconfigure(list(range(rows)), weight=1, uniform='cell', minsize=40)
        self.columnconfigure(list(range(columns)), weight=1, uniform='cell', minsize=40)
        
        window.bind('<Return>', G.findShortestPath)

"""     def return_btn(event):
            print("you hit enter")
            G.findShortestPath
"""

class Graph:
    pass
    def __init__(self,master,size,startX,startY,endX,endY):
        self.graph = [[Node(x,y,"open") for y in range(size)] for x in range(size)]
        self.graph[startX][startY].nodeType = "start"
        self.graph[endX][endY].nodeType = "end"
        self.startNode = self.graph[startX][startY]
        self.endNode = self.graph[endX][endY]

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
w = GraphGUI(window)
w.pack(expand=True, fill=tk.BOTH)
window.title('Path Finder')
window.mainloop()






"""
from tkinter import *

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
master.bind('<Motion>',motion)
msg.pack()
mainloop()"""


"""
This is no linger being used, it was for the user input window but I cant control teh threads
userInput = tk.Tk()

graphSize = 0
startX = 0
startY = 0
endX = 0
endY = 0

def close_window(window):
    graphSize = int(lbl1.get())
    startX = int(lbl2.get())
    startY = int(lbl3.get())
    endX = int(lbl4.get())
    endY = int(lbl5.get())

    window.destroy()

lbl1 = tk.Label(userInput, text="Enter Graph size:")
lbl2 = tk.Label(userInput, text="Enter start x position:")
lbl3 = tk.Label(userInput, text="Enter start y position:")
lbl4 = tk.Label(userInput, text="Enter end x position:")
lbl5 = tk.Label(userInput, text="Enter end y position:")

btn1 = tk.Button(userInput, text="Contruct Graph", command = close_window)

userInput.mainloop()
"""




"""
from tkinter import *

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.pack()
mainloop()
"""
