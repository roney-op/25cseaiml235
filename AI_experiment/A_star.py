import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_cost, current_node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start node to current node
    g_cost = {start: 0}

    # Store the parent of each node
    parent = {start: None}

    while open_list:
        f, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighboring nodes
        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g

                # f(n) = g(n) + h(n)
                f_cost = new_g + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None, None


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}

# Heuristic values h(n)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

# Start and goal
start = 'A'
goal = 'E'

path, cost = a_star(graph, heuristic, start, goal)

print("Shortest Path:", path)
print("Total Cost:", cost)