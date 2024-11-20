# BreadthFirstSearch
# 
'''
 /*********************************************************************************************************************************
     * Time Complexity      : O(V + E), where V is the number of vertices and E is the number of edges.
     * Space Complexity     : O(V), due to the queue and visited array.
     *********************************************************************************************************************************
     * 1. Initialize:
     *      Create a Queue to track nodes for processing.
     *      Create a visited array to avoid revisiting nodes.
     * 2. Enqueue Start Node:
     *      Mark the start node as visited.
     *      Enqueue the start node.
     * 3. Process Queue:
     *      While the queue is not empty:
     *      Dequeue a node, process it (e.g., print or store it).
     *      For each unvisited neighbor, mark it visited and enqueue it.
     *********************************************************************************************************************************/
'''
from collections import deque, defaultdict

class GraphIterative:
    def __init__(self, num_vertex, isDirected):
        self.num_vertex = num_vertex
        self.isDirected = isDirected
        #self.adjList = [[] * self.num_vertex for _ in range(num_vertex)]
        self.adjList = defaultdict(list)

    def addEdge(self, source, destination):
        if destination not in self.adjList[source]:
            self.adjList[source].append(destination)

        if self.isDirected:
            self.adjList[destination].append(source)

    def traverse_bfs(self, startNode):
        self.bfs(startNode)

    def bfs(self, startNode):

        visited = set()
        q = deque()
        visited.add(startNode)
        q.append(startNode)

        while q:
            curr_node = q.popleft()
            print(curr_node, end=" ")
            for curr_node_nei in self.adjList[curr_node]:
                if curr_node_nei not in visited:
                    visited.add(curr_node_nei)
                    q.append(curr_node_nei)


if __name__ == '__main__':
    graph = GraphIterative(4, False)
    graph.addEdge(0,1)
    graph.addEdge(0,2)
    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.traverse_bfs(0)
