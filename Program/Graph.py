from Node import Node
class Graph:
    graph = []
    startNode = Node(-1,-1,"none")
    endNode = Node(-1,-1,"none")

    def __init__(self, nodeGraph):
        self.graph = nodeGraph

    def setStartNode(self, start):
        self.startNode.xPos = start.xPos
        self.startNode.yPos = start.yPos
        self.startNode.nodeType = start.nodeType

    def setEndNode(self, end):
        self.endNode.xPos = end.xPos
        self.endNode.yPos = end.yPos
        self.endNode.nodeType = end.nodeType

