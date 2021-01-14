from tkinter import *
from Node import Node
from Graph import Graph

class UserInterface:

    def printSize(self, event):
        print("whats up")
    
    def display(self, event):
        size = int(self.entry1.get())
        startX = int(self.entry2.get())
        startY = int(self.entry3.get())
        endX = int(self.entry4.get())
        endY = int(self.entry5.get())

        graph = Graph(size,startX,startY,endX,endY)
        graph.displayGraph()

    def findShortestPath(self, event):
        graph.findShortestPath()

    def __init__(self, master):
        lbl1 = Label(root, text="Enter graph size:")
        lbl2 = Label(root, text="Enter the start x value:")
        lbl3 = Label(root, text="Enter the start y value:")
        lbl4 = Label(root, text="Enter the end x value:")
        lbl5 = Label(root, text="Enter the end y value:")

        entry1 = Entry(root)
        entry2 = Entry(root)
        entry3 = Entry(root)
        entry4 = Entry(root)
        entry5 = Entry(root)

        lbl1.grid(row=1, sticky=E)
        lbl2.grid(row=2, sticky=E)
        lbl3.grid(row=3, sticky=E)
        lbl4.grid(row=4, sticky=E)
        lbl5.grid(row=5, sticky=E)

        entry1.grid(row=1, column=5)
        entry2.grid(row=2, column=5)
        entry3.grid(row=3, column=5)
        entry4.grid(row=4, column=5)
        entry5.grid(row=5, column=5)

        printButton = Button(root, text="Print non dynamic size")
        printButton.bind("<Button-1>", self.printSize)
        printButton.grid(row=6,column=10)

        displayBtn = Button(root, text="Display the graph")
        displayBtn.bind("<Button-1>", self.display)
        displayBtn.grid(row=7,column=2)

    


root = Tk()
c = UserInterface(root)
root.geometry('1000x1000')
root.title('Tkinter Testing')
root.mainloop()