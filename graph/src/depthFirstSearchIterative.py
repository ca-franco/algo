# DFS
'''
   /*********************************************************************************************************************************
     * Time Complexity      : O(V + E), where V is the number of vertices and E is the number of edges.
     * Space Complexity     : O(V), due to the visited array and stack used during traversal.
     *********************************************************************************************************************************
     * 1. Initialize:
     *      Use a Stack to track nodes.
     *      Create a visited array.
     * 2. Push Start Node:
     *      Mark the start node as visited.
     *      Push it onto the stack.
     * 3. Process Stack:
     *      While the stack is not empty:
     *          Pop a node, process it.
     *          For each unvisited neighbor, mark it visited and push it onto the stack.
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
        stack = []
        stack.append(v)


        while (len(stack)):
            curr_node = stack.pop()

            if curr_node not in visited:
                print(curr_node, end=" ")
                visited.add(curr_node)

            for nei in self.adjList[curr_node]:
                if nei not in visited:
                    stack.append(nei)

    def traverse_dfs(self, v):
        visited = set()
        self.dfs(v, visited)


if __name__ == "__main__":
    graph = Graph(5, True)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.addEdge(2,4)
    graph.addEdge(3,0)
    graph.addEdge(4,0)
    graph.traverse_dfs(0)
