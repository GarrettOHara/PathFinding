from Node import Node
from Graph import Graph
import sys
class AStarAlgorithm:
    def __init__(self, nodeGraph):
        self.graph = nodeGraph
        self.openList = []
        self.closedList = []

    def startAlgorithm(self):
        self.openList.append(self.graph.getStartNode())

        minValue = self.openList[0].findTotalCost(self.graph.getStartNode(), self.graph.getEndNode())
        for i in range(len(self.openList)):
            minValue = (min(minValue, self.openList[i].
                        findTotalCost(self.graph.getStartNode(), self.graph.getEndNode())))
