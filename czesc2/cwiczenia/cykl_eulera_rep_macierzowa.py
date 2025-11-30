#rep macierzowa, graf spojny, stopnie parzyste
def dfs(G):
    n = len(G)
    def dfs_visit(G, v):
        nonlocal parent, n, cycle, U
        p = parent[v]
        if p is not None:
            G[v][p] = G[p][v] = 0
        while U[v] < n:
            u = U[v]
            U[v]+=1
            if G[v][u] == 1:
                parent[u] = v
                dfs_visit(G, u)
        cycle.append(v)
    U = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    cycle = []
    dfs_visit(G,0)
    return cycle

'''dla reprezentacji listowej:
zeby usunac trzeba trzymac tablice indeksow
chuj wie szczerze o co mu chodzi'''



