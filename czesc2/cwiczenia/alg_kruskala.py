def kruskal(G):
    E = []
    n = len(G)
    for i in range(n):
        for v in G[i]:
            if i<v:
                E.append((w,v,i))
    E = sorted(E)
    en = 0
    s = 0
    fu = union(n)
    for (w,a,b) in E:
        if en == n-1:
            return s
        if fu.find(a) != fu.find(b):
            en += 1
            s += w
            fu.union(a,b)
    return s
