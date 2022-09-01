class Graph:
    def __init__(self):
        self.adjDict={}
    def addVerteX(self,vertex):
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex]=[]
            return True
        return False
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjDict.keys() and vertex2 in self.adjDict.keys():
            self.adjDict[vertex1].append(vertex2)
            self.adjDict[vertex2].append(vertex1)
            return True
        return False
    def deleteEdge(self,vertex1,vertex2):
        if vertex1 in self.adjDict.keys() and vertex2 in self.adjDict.keys():
            try:
                self.adjDict[vertex1].remove(vertex2)
                self.adjDict[vertex1].remove(vertex2)
            except ValueError:
                print(f"{vertex1} and {vertex2} are not connected")
            return True
        return False
    def deleteVertex(self,vertex):
        if vertex in self.adjDict.keys():
            for relatedVertex in self.adjDict[vertex]:
                self.adjDict[relatedVertex].remove(vertex)
            del self.adjDict[vertex]
            return True  
        return False
    def printGraph(self):
        for vertex in self.adjDict:
            print(vertex,"->",self.adjDict[vertex])     

# myGraph=Graph()
# myGraph.addVerteX("IST")
# myGraph.addVerteX("NGD")               
# myGraph.addVerteX("TSA")               
# myGraph.addVerteX("AMS")               
# myGraph.addVerteX("JFK")
# myGraph.addEdge("IST","AMS")
# myGraph.addEdge("AMS","NGD")               
# myGraph.addEdge("IST","TSA")               
# myGraph.addEdge("JFK","NGD")
# myGraph.deleteVertex("IST")
# myGraph.deleteEdge("JFK","NGD")
# myGraph.printGraph()
              
