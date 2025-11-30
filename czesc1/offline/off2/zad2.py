#Jakub Kwiecień
#Rozwiązanie zadania polega na rekurencyjnym zliczaniu inwersji za pomocą merge-sorta.
#W momencie gdy część po prawej stronie jest mniejsza, to zlicza całą lewą strone - index na ktorym jestesmy
#Czas: nlogn
from zad2testy import runtests

def count_inversions(A):
    if len(A) <= 1:
        return 0
    n = len(A)
    mid = n//2
    left = A[:mid]
    right = A[mid:]

    #rekurencja
    inv_left = count_inversions(left)
    inv_right = count_inversions(right)
    inv = 0
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i+=1
            k+=1
        else:
            A[k] = right[j]
            j+=1
            k+=1
            inv += len(left) - i
    while i < len(left):
        A[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        A[k] = right[j]
        j+=1
        k+=1
    return inv + inv_left + inv_right








# Odkomentuj by uruchomic duze testy
runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( count_inversions, all_tests=False )
