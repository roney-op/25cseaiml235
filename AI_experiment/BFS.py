from collections import deque

# Graph represented as an adjacency list
graph = {}

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Create a queue
    visited.add(start)

    print("BFS traversal:", end=" ")

    while queue:
        vertex = queue.popleft()   # Remove front element
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Start BFS from node A
# bfs(graph, 'A') # This call should be commented out or removed if the graph is meant to be populated by user input

# Main program
# The graph is re-initialized here, so the initial graph definition above serves as an example or placeholder.
n = int(input("enter number of vertices:"))

for i in range(n):
  vertex = input(f"enter vertex {i+1}: ")
  neighbors = input(f"enter adjacent vertices of {vertex} (space-separated): ").split()
  graph[vertex] = neighbors
  # Ensure all neighbors are also keys in the graph, even if they have no outgoing edges
  for neighbor in neighbors:
    if neighbor not in graph:
      graph[neighbor] = []

start = ""
while start not in graph:
    start = input("enter starting vertex: ")
    if start not in graph:
        print(f"Error: '{start}' is not a valid starting vertex. Please choose from {list(graph.keys())}")

bfs(graph, start)