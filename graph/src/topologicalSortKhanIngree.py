from collections import deque

class Graph:
    def __init__(self, vertexes, isDirected):
        self.num_vertexes = vertexes
        self.isDirected = isDirected 
        self.adjList = [[] for _ in range(self.num_vertexes)]

    def addEdge(self, source, destination):
        self.adjList[source].append(destination)

    def topoSort(self):
        nodes = {}
        q = deque()

        inDegree = [0] * self.num_vertexes
        # Create indegree for all the vertex from the adjList
        for v in range(self.num_vertexes):
            for depVertexes in self.adjList[v]:
                inDegree[depVertexes] += 1

        # if indegree is zero push it to queue
        for node in range(self.num_vertexes):
            if inDegree[node] == 0:
                q.append(node)

        result = []
        while q:
            node = q.popleft()
            result.append(node)

            # for each vertex reduce indegree 
            for subDependencyVertex in self.adjList[node]:
                inDegree[subDependencyVertex] -= 1

                if inDegree[subDependencyVertex] == 0:
                    q.append(subDependencyVertex)
        return result
                  
if __name__ == "__main__":
    graph = Graph(6, False)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.addEdge(4,5)
    graph.addEdge(5,1)
    graph.addEdge(5,2)
    result = graph.topoSort()
    print(result)
