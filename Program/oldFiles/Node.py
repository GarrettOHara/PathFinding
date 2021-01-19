class Node:
    def __init__(self,x,y,nodeType):
        self.xPos = int(x)
        self.yPos = int(y)
        self.nodeType = str(nodeType)

        self.h = 0
        self.g = 0
        self.f = 0
    
    def __eq__(self,node):
        if((self.xPos == node.xPos) and (self.yPos == node.yPos)):
            return True
        else:
            return False
    
    def __str__(self):
        return "(" + str(self.xPos) + "," + str(self.yPos) + "," + self.nodeType + ")"