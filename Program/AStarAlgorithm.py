from Node import Node
from Graph import Graph
import sys
class AStarAlgorithm:
    openList = []
    closedList = []

    def __init__(self, nodeGraph):
        self.graph = nodeGraph

    def startAlgorithm(self):

        self.openList.append(self.graph.startNode)
        self.openList[0].findHeuristic(self.graph.endNode)
        self.openList[0].findCurrentCost(self.graph.startNode)
        minValue = self.openList[0].findTotalCost()
        for i in range(len(self.openList)):
            self.openList[i].findHeuristic(self.graph.endNode)
            self.openList[i].findCurrentCost(self.graph.startNode)
            minValue = min(minValue, self.openList[i].findTotalCost())