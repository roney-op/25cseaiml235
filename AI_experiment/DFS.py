
# function to perform DFS

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Input number of vertices
n = int(input("Enter the number of vertices: "))

graph = {}

# Input adjacency list for each vertex
for i in range(n):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors

# Input starting vertex
start = input("Enter the starting vertex for DFS: ")

visited = set()


print("DFS Traversal:")
dfs(graph, start, visited)