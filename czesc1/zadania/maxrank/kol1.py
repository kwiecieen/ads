from kol1testy import runtests

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

def maxrank(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    quick_sort(T, 0, n-1)
    mrank = 0
    i = n-1
    while i>mrank:
        index = T[i][1]
        while i>0 and T[i-1][0] == T[i][0]:
            i -= 1


        rank = index - (n-i-1)
        if rank > mrank:
            mrank = rank
        i-=1

    return mrank





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )

# T = [5, 3, 9, 4]
# print(maxrank(T))
