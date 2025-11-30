def has_cycle_undirected(graph):
    visited = [False] * len(graph)

    def dfs(u, parent):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for u in range(len(graph)):
        if not visited[u]:
            if dfs(u, -1):
                return True
    return False


def has_cycle_directed(graph):
    n = len(graph)
    color = [0] * n  # 0 = white, 1 = gray, 2 = black

    def dfs(u):
        color[u] = 1  # gray
        for v in graph[u]:
            if color[v] == 1:
                return True  # back edge -> cycle
            if color[v] == 0:
                if dfs(v):
                    return True
        color[u] = 2  # black
        return False

    for u in range(n):
        if color[u] == 0:
            if dfs(u):
                return True
    return False


graph_with_cycle = [
    [1, 2],    # 0
    [0, 3],    # 1
    [0, 3],    # 2
    [1, 2]     # 3
]


graph_without_cycle = [
    [1],       # 0
    [0, 2],    # 1
    [1]        # 2
]

print(has_cycle_undirected(graph_with_cycle))
print(has_cycle_undirected(graph_without_cycle))

graph_with_cycle = [
    [1],       # 0
    [2],       # 1
    [0]        # 2
]



graph_without_cycle = [
    [1],       # 0
    [2],       # 1
    []         # 2
]

print(has_cycle_directed(graph_with_cycle))
print(has_cycle_directed(graph_without_cycle))
