from asyncio import PriorityQueue

#taki se ten algorytm, trzeba znalezc lepszy
# zlozonosc czasowa O(V^2)
def dijkstra(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    dist = [float('inf')] * n
    dist[s] = 0
    que = PriorityQueue()
    que.put((0, s))
    while not que.empty():
        x = float('inf')
        y = -1
        for u in range(n):
            if not visited[u] and dist[u] < x:
                x = dist[u]
                y = u
        d = x
        u = y
        if visited[u]: continue
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and not visited[v] and relax(u, v, dist, parent):
                que.put((d+G[u][v], v))
    return dist, parent

def relax(u, v, dist, parent):
    nonlocal G
    if dist[v] > dist[u] + G[u][v]:
        dist[v] = dist[u] + G[u][v]
        parent[v] = u
        return True
    return False
