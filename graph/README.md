# Graph
## Graph Traversal
    Multiple ways we can depict the graph traversal few are
    - Edge List
    Stores all the edges in the list and we need to parse through the list inorder to find the 
    required edge. As mentioned in the [Time and space complexity consolidation](#Time-and-space-complexity-consolidation)
    - Adjacent Matrix
    - Adjacent List
    - Adjacent Map/Set

### Time and space complexity consolidation
    | Type of representation | Time complexity      | Space complexity |
    |------------------------|----------------------|------------------|
    | edge list              |  O(|E|)=O(m)         |  O(n(vertices) + |
    |                        | to find neighbours   |    m(edges))     |
    |                        | of all vertexes      |                  |
    |                        |O(m.n)=O(n^2.n)=O(n^3)|                  |                  
    |------------------------|----------------------|------------------|
    | Adj List               |  O(m) if m           |  O(m+n)          |
    |                        |   edges are there    |                  |
    |                        |                      |                  |
    |------------------------|----------------------|------------------|
    | Adj Matrix             |  O(n)                | O(n^2) =n(n-1)/2 |
    |------------------------------------------------------------------|  
    
## Graph Glossary
1. Directed Edges.
    - Ordered pair of vertices(u,v).
    - First vertex u is the origin.
    - Second vertex v is the destination.

![Ex: One way Road](https://github.com/ca-franco/algo/blob/main/assets/images/directededge.png)

2. Undirected Edges.
    - Unordered pair of vertices(u,v)
   
![Ex: Rail Road](https://github.com/ca-franco/algo/blob/main/assets/images/undirectededge.png)

3. Directed Graph
    - All the edges are directed.

![Ex: Route network](https://github.com/ca-franco/algo/blob/main/assets/images/directedgraph.png)

4. Undirected Graph
    - All the edges are undirected.

![Ex: Flight network](https://github.com/ca-franco/algo/blob/main/assets/images/undirectedgraph.png)
 
5. Adjecent Vertices
    - When 2 vertices are connected the connected vertices are called adjecent and edges are called 
      `incident on` both vertices.

6. Graph as Tree
    - Graph with no cycle `Tree`. A tree is Acyclic connected graph.

![Ex: Tree as Graph](https://github.com/ca-franco/algo/blob/main/assets/images/treegraph.png)

7. Self loop
    - edge that connects to itself.


![Ex: Self Loop](https://github.com/ca-franco/algo/blob/main/assets/images/selfloop.png)
 
8. Degree
    - Degree of vertex is the number of edges that are `incident on` it

9. Subgraph
    - A subgraph is a subset of a graph's edge (with associated vertices) that form a graph.

10. Path
    - A path is in a graph if sequence of adjecent vertices. simple path if path has no
    repeated vertices in the graph.

![Ex: Path](https://github.com/ca-franco/algo/blob/main/assets/images/path.png)

11. Cycle
    - cycle is path with adjecent vertices with no repeated vertices and `simple cycle` if
    no repeated vertices except for starting and ending.

![Ex: cycle](https://github.com/ca-franco/algo/blob/main/assets/images/cycle.png)

12. Strongly connected graph
    - If connection between two vertices (u,v) and (v,u) is present then 
    the connectivity is strong and strongly connected graph.

13. Connected components
    - In a connected graph if all the vertices are not connected, it is called connected components.

![Ex: connectedcomponents](https://github.com/ca-franco/algo/blob/main/assets/images/connectedcomponents.png)

14. Directed Acyclic Graph
    - The vertices for DAG if all the vertices are connected and if there is no cycle it is called DAG.

![Ex: dag](https://github.com/ca-franco/algo/blob/main/assets/images/dag.png)

15. Weighted Graph
    - A graph which has weight assigned for edges is called weigthed graph.

![Ex: dag](https://github.com/ca-franco/algo/blob/main/assets/images/weightedgraph.png)

16. Shortest path
    - to know a path between u,v vertices if there is a shortest path, so that we 
    can define minimum number of edges.

17. Forest
    - Disjointed set of tree

18. Spanning Tree / Spanning forest
    - In a sub graph if it has all the vertices and is a single tree. spanning forest is a union of 
    multiple tree under connected components.

19. Bipartite graph
    - a grapgh whore vertices can be divided into two sets such that all edges connect a vertex in one set with a vertex in other set.

![Ex: dag](https://github.com/ca-franco/algo/blob/main/assets/images/bipartitegraph.png)

20. Complete graph.
    - garph with all the edges present are called complete graph

21. Sparse graph
    - Graph with very few edges is call sparse graph. edges < |v|

22. Dense graph
    - Graph with only very few edges missing.

23. Total edges in undirected graph
    - Total number of edges in undirected graph is v(v-1)/2 because any vertices can connect to any.
    
