import networkx as nx
from collections import deque

# Create a new, empty graph
G = nx.Graph()

# Add edges to the graph (this also adds the nodes)
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
G.add_edges_from(edges)

# Print the nodes and edges of the graph
print("Nodes of the graph:")
print(G.nodes())
print("Edges of the graph:")
print(G.edges())

# Function to perform BFS
def bfs(graph, start_node):
    visited = set()  # A set to keep track of visited nodes
    queue = deque([start_node])  # A queue to hold the nodes to visit
    
    print(f"BFS starting from node {start_node}:")
    while queue:
        # Dequeue a node from the queue
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append(neighbor)
    print()  # For a new line at the end of the BFS

# Perform BFS on the graph starting from node 1
bfs(G, 1)
