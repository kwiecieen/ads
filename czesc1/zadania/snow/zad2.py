from zad2testy import runtests

def snow(S):
    def quick_sort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quick_sort(A, p, q - 1)
            quick_sort(A, q + 1, r)

    def partition(A, p, r):
        pivot = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] >= pivot:  # Sortujemy malejąco
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    quick_sort(S, 0, len(S) - 1)  # Sortujemy malejąco

    snow = 0
    top = 0
    for i in range(len(S)):
        if S[i] > top:
            snow += (S[i] - top)
            top += 1  # Warstwa lodu rośnie

    return snow

# Uruchomienie testów
runtests(snow, all_tests=True)
