from kol1testy import runtests

def ksum(T, k, p):
    n = len(T)
    suma = 0
    def quick_select(A, p, r, k):
        if p < r:
            q = partition(A, p, r)
            if q == k:
                return A[q]
            elif q > k:
                return quick_select(A, p, q - 1, k)
            else:
                return quick_select(A, q + 1, r, k)
        return A[p]  # Jeśli p == r, to mamy tylko jeden element

    def partition(A, p, r):
        pivot = A[r]
        i = p - 1  # i wskazuje na ostatni element mniejszy od pivota
        for j in range(p, r):
            if A[j] >= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    for i in range(n-p+1):
        A = T[i:i+p]
        suma+=quick_select(A, 0, len(A)-1, k-1)

    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=False )
