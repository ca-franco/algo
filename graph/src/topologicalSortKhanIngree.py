from collections import deque
'''
 /*********************************************************************************************************************************
     * Time Complexity      : O(V + E), where V is the number of vertices and E is the number of edges.
     * Space Complexity     : O(V), due to the in-degree array, adjacency list, and the queue used during traversal.
     *********************************************************************************************************************************
     * 1. Calculate In-Degree:
     *      Initialize an array to store in-degrees for all vertices.
     *      For each vertex, traverse its adjacency list and increment the in-degree of adjacent vertices.
     * 2. Initialize Queue:
     *      Add all vertices with in-degree 0 (no dependencies) to a queue.
     * 3. Process Queue:
     *      While the queue is not empty:
     *          Dequeue a vertex, add it to the topologically sorted list.
     *          For each adjacent vertex, reduce its in-degree by 1.
     *          If an adjacent vertex's in-degree becomes 0, add it to the queue.
     * 4. Check for Cycles:
     *      If all vertices are processed (sorted list contains all vertices), print the topological order.
     *      If not, there is a cycle in the graph.
     *********************************************************************************************************************************/
'''

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
