from collections import deque, defaultdict

def kahns_algorithm(num_nodes, edges):
    # Build the graph and calculate in-degrees
    in_degree = [0] * num_nodes
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        in_degree[dest] += 1

    # Find all vertices with zero in-degree
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) == num_nodes:
        return top_order
    else:
        return []  # Cycle detected or incomplete sorting
    

def dfs(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(node)

def topological_sort_dfs(num_nodes, edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)

    visited = [False] * num_nodes
    stack = []

    for node in range(num_nodes):
        if not visited[node]:
            dfs(node, graph, visited, stack)

    return stack[::-1]  # Return reversed stack
