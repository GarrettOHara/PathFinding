from Node import Node
class Graph:

    def __init__(self, size):
        self.graph = [size][size]
        self.startNode = Node(-1,-1,"none")
        self.endNode = Node(-1,-1,"none")

    def populate(self, startX, startY, endX, endY):
        for x in range(len(graph)):
            for y in range(len(graph[0])):
                if(x == startX and y == startY):
                    temp = Node(x,y,"start")
                    self.graph[x][y] = temp
                    self.startNode = temp
                else if(x == endX and y == endY):
                    temp = Node(x,y,"end")
                    self.graph[x][y] = temp
                    self.endNode = temp
                else:
                    self.graph[x][y] = Node(x,y,"open")

    #setters and getters