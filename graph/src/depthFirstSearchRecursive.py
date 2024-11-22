# DFS
'''
/*********************************************************************************************************************************
     * Time Complexity      : O(V + E), where V is the number of vertices and E is the number of edges.
     * Space Complexity     : O(V), due to the recursive call stack and the visited array.
     *********************************************************************************************************************************
     * 1. Define Recursive Helper:
     *      Mark the current node as visited.
     *      Process the current node.
     *      Recursively call DFS on each unvisited neighbor.
     * 2. Call Helper:
     *      For each unvisited node, call the helper function to handle disconnected components.
     *********************************************************************************************************************************/
'''

class Graph:
    def __init__(self, vertices, isDirected):
        self.vertices = vertices
        self.isDirected = isDirected
        self.adjList = [[] for _ in range(vertices)]


    def addEdge(self, source, destination):
        if source not in self.adjList:
            self.adjList[source].append(destination)
        if self.isDirected:
            self.adjList[destination].append(source)

    def dfs(self, v, visited):

        visited.add(v)
        print(v, end=" ")

        for nei in self.adjList[v]:
            if nei not in visited:
                self.dfs(nei, visited)

    def traverse_dfs(self, v):
        visited = set()
        self.dfs(v, visited)



if __name__ == "__main__":
    graph = Graph(5, False)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.addEdge(2,4)
    graph.addEdge(3,0)
    graph.addEdge(4,0)
    graph.traverse_dfs(3)
