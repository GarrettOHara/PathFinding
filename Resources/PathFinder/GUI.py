import tkinter as tk
import sys
import math

class Node(tk.Frame):
    BLOCK_COLOR = "gray"
    CLEAR_COLOR = "white"
    def __init__(self,master=None,**kwargs): #,x,y,nodeType
        super().__init__(master, **kwargs)
        self.config(borderwidth=1, 
                    bg=self.CLEAR_COLOR, 
                    relief=tk.RAISED)
        self.bind('<1>', self.on_click)

        # self.xPos = int(x)
        # self.yPos = int(y)
        # self.nodeType = str(nodeType)
        # self.size = 50

        self.h = 0
        self.g = 0
        self.f = 0

    def on_click(self, event=None):
        if self['bg'] == self.CLEAR_COLOR:
            self['bg'] = self.BLOCK_COLOR
        else:
            self['bg'] = self.CLEAR_COLOR
    
    def __eq__(self,node):
        if((self.xPos == node.xPos) and (self.yPos == node.yPos)):
            return True
        else:
            return False

class Graph(tk.Frame):#, start, end):
    def __init__(self, master=None, rows=1, columns=1, **kwargs):
        super().__init__(master, **kwargs)
        # self.rows = rows
        # self.column = columns
        # self.startx = startx
        # self.starty = starty
        # self.endx = endx
        # self.endy = endy

        for row_num in range(rows):
            for col_num in range(columns):
                f = Node(self)#,row_num,col_num,"open"
                f.grid(row=row_num, column=col_num, sticky='nsew')

        self.rowconfigure(list(range(rows)), 
                          weight=1, uniform='cell', 
                          minsize=40)
        self.columnconfigure(list(range(columns)), 
                             weight=1, uniform='cell', 
                             minsize=40)

