#ZASTOSOWANIA BFS:
#-znajdowanie najkrótszych ścieżek
#-sprawdzanie spójności grafu
#-sprawdzanie czy graf ma cykl
#-sprawdzanie czy graf jest dwudzielny

#zlozonosc O(V+E), dla reprezentacji przez listy sąsiedztwa, O(V^2) dla macierzy sąsiedztwa
#pseudokod


from collections import deque

#G = [[1,2],[2,4,5],[1,3,7]...]
def BFS(G, s): #G = (V,E), s to jakis wierzcholek
    #kazdy wierzcholek ma pola: visited, parent, d(odleglosc)
    #mamy także kolejkę Q(stan, gdzie obecnie jest fala uderzeniowa)
    Q = deque()
    #for v in V:
        #v.visited = False
        #v.parent = None
        #v.d = float('inf')
    n = len(G) # bardziej dla pythona
    visited = [False] * n
    parent = [None] * n
    d = [float('inf')] * n
    s.d = 0
    s.visited = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]: #M to zbior sasiadow
            if not v.visited:
                v.visited = True
                v.parent = u
                v.d = u.d + 1
                Q.append(v)


