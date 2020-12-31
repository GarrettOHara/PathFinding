from Node import Node
from Graph import Graph
from queue import PriorityQueue
import sys
class AStarAlgorithm:
    def __init__(self, nodeGraph):
        self.graph = nodeGraph
        self.openList = []
        self.closedList = []

    def startAlgorithm(self):
        self.openList.append(self.graph.startNode)
        pq = PriorityQueue()
        pq.put(self.graph.startNode)

        minValue = self.openList[0].findTotalCost()
        for i in range(len(self.openList)):
            minValue = (min(minValue, self.openList[i].findTotalCost()))
