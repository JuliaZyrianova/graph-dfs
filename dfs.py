# Depth-First Search algorithm implementation
# Returns path length from start to end vertex
# Raises ValueError if vertices are not in graph
def dfs_path_length(graph, start, end):
    # Validate input vertices
    if start not in graph or end not in graph:
        raise ValueError("Start or end vertex not in graph")
    
    visited = []  # Tracks visited vertices
    stack = [(start, 0)]  # Stack with tuples (vertex, current_path_length)
    
    while stack:
        vertex, path_length = stack.pop()
        if vertex == end:
            return path_length
        if vertex not in visited:
            visited.append(vertex)
            # Add all unvisited neighbors to stack
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    stack.append((neighbor, path_length + 1))
    return -1  # Return -1 if no path exists

# Пример использования
if __name__ == "__main__":
    graph = {
        1: [3],
        2: [4],
        3: [1],
        4: [2]
    }
    print(dfs_path_length(graph, 2, 4))  # Вывод: 1