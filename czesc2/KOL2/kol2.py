from queue import PriorityQueue


def lets_roll(start_city, flights, resorts):
    def convert_edges_to_adj_list(edges):
        if not edges:
            return []
        n = max(max(u, v) for u, v, _ in edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        return graph

    def dijkstra_with_forbidden(G, s, forbidden_cities):
        n = len(G)
        inf = float('inf')
        dist = [inf] * n
        dist[s] = 0
        pq = PriorityQueue()
        pq.put((0, s))

        while not pq.empty():
            d, u = pq.get()
            if d != dist[u]:
                continue
            for v, w in G[u]:
                # Nie można przechodzić przez miasta z odwiedzonymi ośrodkami
                if v in forbidden_cities:
                    continue
                new_d = d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    pq.put((new_d, v))
        return dist

    graph = convert_edges_to_adj_list(flights)

    visited_resorts = set()
    total_cost = 0

    # Grzegorz odwiedza ośrodki jeden po drugim
    while len(visited_resorts) < len(resorts):
        # Miasta z już odwiedzonymi ośrodkami są zabronione do przechodzenia

        # Znajdź odległości z miasta startowego z ograniczeniami
        distances = dijkstra_with_forbidden(graph, start_city, visited_resorts)

        # Wybierz najbliższy nieodwiedzony ośrodek
        best_resort = None
        best_cost = float('inf')

        for resort in resorts:
            if resort not in visited_resorts:
                cost = distances[resort]
                if cost < best_cost:
                    best_cost = cost
                    best_resort = resort

        if best_resort is None or best_cost == float('inf'):
            break  # Nie można dotrzeć do żadnego ośrodka

        # Koszt podróży tam i z powrotem
        total_cost += 2 * best_cost
        visited_resorts.add(best_resort)

    return total_cost




# Uruchomienie testów
from kol2testy import runtests

runtests(lets_roll, all_tests=True)



