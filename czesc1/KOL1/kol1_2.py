#JAKUB KWIECIEŃ
#algorytm sortuje tablicę T za pomocą quick sorta, następnie sprawdza czy różnica między dwoma palikami jest większa od D
#jeśli para palików jest wystarczająco daleko to dodaje +1 do cnt, następnie zwraca ten cnt
#zlożoność czasowa: nlogn
from kol1testy import runtests
def ogrodzenie(M, D, T):
    def merge_sort(A):
        n = len(A)
        if n<=1:
            return A
        mid = n//2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
                k += 1
            else:
                A[k] = right[j]
                j += 1
                k+=1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return A

    n = len(T)
    merge_sort(T)
    cnt = 0
    for i in range(n-1):
        if T[i+1]-T[i] > D:
            cnt+=1
    return cnt




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )
