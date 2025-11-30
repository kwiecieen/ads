def is_connected(G):
    n = len(G)
    visited = [False for _ in range(n)]
    def DFS_visit(v):
        nonlocal visited, G
        visited[v] = True
        for n_v in range(n):
            if G[v][n_v] == 1 and not visited[n_v]:
                DFS_visit(n_v)
    for is_visited in visited:
        if not is_visited:
            return False
    return True

