from collections import deque

G = [[2,3,4], #0
     [3,4],   #1
     [0],     #2
     [0,1],   #3
     [0,1]]   #4

def is_bipartite(G):
    n = len(G)
    Q = deque()
    visited = [False for _ in range(n)]
    color = [0 for _ in range(n)]
    visited[0] = True
    Q.append(0)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)
                color[v] = 1 - color[u]
            elif visited[v] and color[v] == color[u]:
                return False
    return True

print(is_bipartite(G))

