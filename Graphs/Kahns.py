from collections import deque

#Kahn’s Algorithm for Topological Sorting is a method used to order the vertices of a directed graph 
# in a linear order such that for every directed edge from vertex A to vertex B, A comes before B in the order. 
# The algorithm works by repeatedly finding vertices with no incoming edges, removing them from the graph, 
# and updating the incoming edges of the remaining vertices. This process continues until all vertices have been ordered.

#In order to perform Kahn's algorithm you need an adjacency list of the incoming edges for each node.
#If only given the outgoing edges, you can recreate this, and count the indegree's in the same loop.
def get_indegrees(outgoing_adj_array):
    nodes = len(outgoing_adj_array)
    indegree = [0] * nodes
    incoming_adj_array = [[] for _ in range(nodes)]
    for i in range(nodes):
        for node in outgoing_adj_array[i]:
            indegree[i] += 1 #incrementing the count of incoming edges for i
            incoming_adj_array[node].append(i) #appending the incoming edge i to the original outgoing node
    return indegree, incoming_adj_array

# The queue is initialised to contain all node with 0 incoming edges, ie indegree == 0
# Function to return list containing vertices in Topological order using BFS
def topological_sort_bfs(adj, V):
    # Vector to store indegree of each vertex
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1

    # Queue to store vertices with indegree 0
    q = deque([i for i in range(V) if indegree[i] == 0])

    result = []
    while q:
        node = q.popleft()
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, push it to the queue
            # Because it only appends items with a new indegree == 0, it will never include cyclic nodes
            if indegree[adjacent] == 0:
                q.append(adjacent)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result


if __name__ == "__main__":
    n = 7  # Number of nodes

    # Edges
    edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 5], [3, 0], [4, 5]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(n)]

    # Constructing adjacency list
    for edge in edges:
        adj[edge[0]].append(edge[1])

    # Performing topological sort
    print("Topological sorting of the graph:", end=" ")
    result = topological_sort_bfs(adj, n)

    # Displaying result
    for vertex in result:
        print(vertex, end=" ")


    #Another example
    n = 7  # Number of nodes
    edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 5], [3, 0], [4, 5]]

    #This option creates the indgree and the edges all inside the same loop
    indegree = [0] * n
    adj = [[] for _ in range(n)]
    for edge in edges:
        indegree[edge[1]] += 1
        adj[edge[0]].append(edge[1])

    def top_bfs(indegree, adj, n):
        queue = deque([i for i in range(n) if indegree[i] == 0])
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for neighbour in adj[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(result) != n:
            return print("there is a cycle in this graph")
        
        return result






