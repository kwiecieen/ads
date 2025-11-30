#  ZNALEZC SPOSOB JAK ZROBIC Z TEGO ZAWSZE N LOG N
#zaczynamy od tablicy A
#funkcja partition
#znajduje piwot
#wszystko co znajdzie sie po lewej od piwota bedzie od niego mniejsze, a po prawej wieksze
#sortujemy rekurencyjnie obie czesci
#w wersji optymistycznej: nlogn
#w wersji pesymistycznej: n^2 (mala szansa)
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r) #rekurencja ogonowa, bo wywola samego siebie
#mamy tablice A, jej koniec i początek
def partition(A, p, r):
    pivot = A[r]
    i = p - 1    #i wkazuje na pierwszy element po lewej
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

A = [4,5,7,1,2,54,37,30]
quick_sort(A, 0, len(A)-1)
print(A)

#istnieje inna wersja partition, podobno szybsza
