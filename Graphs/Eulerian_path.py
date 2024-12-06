from collections import Counter
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

def get_node_degrees(graph:List[List[int]]):
    in_count = Counter([pair[1] for pair in graph])
    out_count = Counter([pair[0] for pair in graph])
    edge_count = len(graph)
    return in_count, out_count, edge_count
graph = [[5,1],[4,5],[11,9],[9,4]]
inarr, outarr, edgecount = get_node_degrees(graph)
print(inarr,outarr,edgecount)

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

#If you find a Eulerian path, but not circuit, the next steps is to find the start and end node of that path.
#This can be done by backtracking a dfs search each of the nodes and seeing if you visited every edge once.
#You can reuse the out degrees count for this, and reduce the count by 1 each time you traverse an edge.
#When the dfs gets stuck (ie no outgoing edges, ie out count = 0) you backtrack until you are able to traverse another edge.

#This is known as Hierholzer's algorithm. Which has Time complexity is O(E) - edges.