from collections import Counter, defaultdict, deque
from typing import List

#Eulerian Path is a path of edges that visits all the edges in a graph exactly once.
#Not every graph has a Eulerian path.

#Eulerian circuit (Eulerian cycle) is a Eulerian path which starts and ends on the same node.
#If a graph has a Eulerian circuit, you can start your Eulerian path from any node.
#If a graph doesn't contain a Eulerian cycle then you may not be able to return to the start node, 
# or you won't be able to visit all the edges

#All graph with an Eulerian circuit also has an Eulerian path

#In determining whether a graph contains a Eulerian path/circuit, you need to know if it's an
#directed or undirected graph, and what their node degrees are.

#An undirected graph node degree is the number of edges attached to a node.
#A directed graph node degree is split into 2: 
# in degree - number of incoming edges
# out degree - number of outgoing edges

def get_node_degrees(graph:List[List[int]]) -> tuple[defaultdict, defaultdict, deque]:
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    adjacency_matrix = defaultdict(deque)

    for start, end in graph:
        adjacency_matrix[start].append(end)
        in_degree[end] += 1
        out_degree[start] += 1

    return in_degree, out_degree, adjacency_matrix

graph = [[5,1],[4,5],[11,9],[9,4]]
inarr, outarr, adjacency_matrix = get_node_degrees(graph)
print(inarr, outarr, adjacency_matrix)

#This therefore creates a matrix of required properties depending on the graph type your dealing with
#and whether you're interested in finding a Eulerian path or circuit.

#1. Eulerian Circuit on a Undirected graph -
#   Every node has an even degree.
#2. Eulerian Path on a Undirected graph - 
#   Either every node has even degree or exactly two nodes had odd degree.
#3. Eulerian Circuit on a Directed graph - 
#   Every node has equal indegree and outdegree.
#4. Eulerian Path on a Directed graph -
#   At most one node has (outdegree) - (indegree) = 1. 
#   And at most one node has (indegree) - (outdegree) = 1.
#   And all other verticies have equal in and out degrees.
#NOTE: An Eulerian Path is still valid if singleton nodes exist in the graph with 0 edges.
#However, a graph with more than 1 non-connected nodes and edges group cannot have a Eulerian Path.

#The 1st step to discovering a Eulerian path in a directed graph is to count the number of 
#in and out degrees for each node. 
#Once you have that you can compare against the above requirements to ensure it has a Eulerian path.
def has_eulerian_path(graph:List[List[int]]) -> bool:
    inarr, outarr, _ = get_node_degrees(graph)
    diffs = 0
    for k, v in inarr.items():
        diff = v - outarr.get(k, 0)
        if diff > 1:
            return False
        elif diff == 1:
            diffs += 1
            if diffs > 1:
                return False
    diffs = 0
    for k, v in outarr.items():
        diff = v - inarr.get(k, 0)
        if diff > 1:
            return False
        elif diff == 1:
            diffs += 1
            if diffs > 1:
                return False
    return True

graph = [[5,1],[4,5],[11,9],[9,4]]
has_path = has_eulerian_path(graph)
print(has_path)

#If you find a Eulerian path, but not circuit, the next steps is to find the start and end node of that path.
#This can be done by looking at the differences in the incoming and outgoing edges of the graph.
#The node with 1 greater outgoing edges to incoming edges is our start point, and the node with 1 greater number of incoming
#edges to outgoing edges will be our end node.
#If all nodes have equal degree's then we have a eulerian circuit - see point 3 above for logic - which means we can start at any node.

#This function assumes that Eulerian path has already been found.
def find_start_node(graph:List[List[int]]):
    inarr, outarr, _ = get_node_degrees(graph)
    start = 0
    for k, v in outarr.items():
        diff = v - inarr.get(k, 0)
        if diff == 1:
            return k
        elif v > 0:
            start = k
    return start

graph = [[5,1],[4,5],[11,9],[9,4]]
start = find_start_node(graph)
print(start)
    
#Next, we need to traverse the path. If done using a naive DFS from our start and end nodes, this won't give us the correct answer.
#However, this can be done by backtracking a dfs search for each of the nodes and seeing if you visited every edge once.
#You can reuse the out degrees count for this, and reduce the count by 1 each time you traverse an edge.
#When the dfs gets stuck (ie no outgoing edges, ie out count = 0) you backtrack until you are able to traverse another edge.

#This is known as Hierholzer's algorithm. Uses a stack instead of DFS recursion to traverse the graph.
#Appends to the left of the path so that it is returned in the correct order.
#Time complexity - O(V + E)
#Space complexity - O(V + E)

def hierholzers(graph:List[List[int]]) -> List[List[int]]:
    inarr, outarr, adj_matrix = get_node_degrees(graph)

    has_path = has_eulerian_path(graph)
    if not has_path:
        return None
    
    start = find_start_node(graph)
    path = deque()
    stack = [start]
    while stack:
        node = stack[-1]
        if adj_matrix[node]:
            next = adj_matrix[node].popleft()
            stack.append(next)
        else:
            path.appendleft(node)
            stack.pop()

    result = [[path[i - 1], path[i]] for i in range(1, len(path))]
    return result

#dfs solution uses post order dfs traversal to visit all of the nodes.
def dfs(graph:List[List[int]]) -> List[List[int]]:
    inarr, outarr, adj_matrix = get_node_degrees(graph)

    has_path = has_eulerian_path(graph)
    if not has_path:
        return None
    
    start = find_start_node(graph)
    path = deque()
    
    def postorder_dfs(node):
        while adj_matrix[node]:
            next = adj_matrix[node].popleft()
            postorder_dfs(next)
        path.appendleft(node)
    
    postorder_dfs(start)

    result = [[path[i - 1], path[i]] for i in range(1, len(path))]
    return result

graph = [[5,1],[4,5],[11,9],[9,4]]
start = hierholzers(graph)
print(start)
