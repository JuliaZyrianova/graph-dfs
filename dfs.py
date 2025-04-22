def dfs_path_length(graph, start, end):
    if start not in graph or end not in graph:
        raise ValueError("Start or end vertex not in graph")
    
    visited = []
    stack = [(start, 0)]
    
    while stack:
        vertex, path_length = stack.pop()
        if vertex == end:
            return path_length
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    stack.append((neighbor, path_length + 1))
    return -1

# Пример использования
if __name__ == "__main__":
    graph = {
        1: [3],
        2: [4],
        3: [1],
        4: [2]
    }
    print(dfs_path_length(graph, 2, 4))  # Вывод: 1