#ZASTOSOWANIA:
#-sortowanie topologiczne
#-znajdowanie cyklu eulera
#-znajdowanie silnie wspólnych składowych
#-znajdowanie mostów i punktów artykulacji
#-prawie wszystko co BFS tylko bez najkrotszych sciezek


#pseudokod
def DFS(G):
    def DFSvisit(G,v):
        nonlocal time
        v.visited = True
        time += 1 #czas odwiedzenia
        for u in G[v]: #G[v] to zbior sąsiadow
            if not u.visited:
                u.parent = v
                DFSvisit(G,u)
        time += 1 #czas przetworzenia

    time = 0
    for v in V:
        v.visited = False
        v.parent = None
    for v in V:
        if not v.visited:
            DFSvisit(G,v)
