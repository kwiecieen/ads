#mając tablicę A oraz liczbę k, chcemy obliczyć wartosc, ktora bylaby na pozycji k po posortowaniu
def quick_select(A, p, r, k):  #O(n)
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
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# Przykładowa tablica i wywołanie funkcji
A = [4, 5, 7, 1, 2, 54, 37, 30]
k = 3  # Szukamy elementu na pozycji k (0-indeksowana)
result = quick_select(A, 0, len(A) - 1, k)
print(f"{k}-ty najmniejszy element to: {result}")




