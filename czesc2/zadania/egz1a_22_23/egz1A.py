
from egz1Atesty import runtests
from queue import PriorityQueue

def gold(G,V,s,t,r):
    def dijkstra(Gr,s):
        n = len(Gr)
        q = PriorityQueue()
        dist = [float("inf") for _ in range(n)]
        dist[s] = 0
        q.put((0, s))

        while not q.empty():
            distance, u = q.get()
            for v, c in Gr[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    q.put((dist[v], v))
        return dist
    n = len(G)
    Gr = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(len(G[i])):
            Gr[i].append(G[i][j])
            Gr[i+n].append((G[i][j][0]+n,2*G[i][j][1]+r))
        Gr[i].append((i+n,-V[i]))
    weights = dijkstra(Gr,s)
    return weights[t+n]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
