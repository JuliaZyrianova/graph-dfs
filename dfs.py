def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in graph:  # Check if vertex is in the graph
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    return visited

# Пример использования
if __name__ == "__main__":
    graph = {
        1: [3],
        2: [4],
        3: [1],
        4: [2]
    }
    print(dfs(graph, 1))  # Вывод: [1, 3]