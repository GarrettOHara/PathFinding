from Node import Node
from Graph import Graph
class AStarAlgorithm:
    openList = []
    closedList = []

    def addStartNode(self, start):
        self.openList.append(start)
