from Node import Node
from Graph import Graph
from queue import PriorityQueue
import sys
class AStarAlgorithm:
    def __init__(self, nodeGraph):
        self.graph = nodeGraph
        self.openList = []
        self.closedList = []

    def findGCost(self, closedList):
        g = 1

    def startAlgorithm(self):
        #append start node to open list
        self.openList.append(self.graph.startNode)
        pq = PriorityQueue()
        pq.put(self.graph.startNode)
        while(not (self.openList.count == 0)):
            #pop off the top element of the priority queue
            #create a new node, call it q, we generate all adjacent nodes
            #we loop thru each child and create the base cases
                #if this is the end, alrdy in openList/closedList
            print("iterate")
            q = pq.get()
            qAdjacent = self.graph.getAdjacentNodes(q)
            for node in qAdjacent:
                if(node.nodeType == "end"):
                    self.openList.clear()
                    self.closedList.append(node)
                    break
                    #stop algorithm
                elif(node in self.openList) or \
                     (node in self.closedList):
                    print("elif")
                    continue
                else:
                    print("else")
                    pq.put(node)
                    self.openList.append(node)
        print("made it here")
    """
        minValue = self.openList[0].findTotalCost()
        for i in range(len(self.openList)):
            minValue = (min(minValue, self.openList[i].findTotalCost()))
    """