#JAKUB KWIECIEŃ
#algorytm sortuje tablicę T za pomocą quick sorta, następnie sprawdza czy różnica między dwoma palikami jest większa od D
#jeśli para palików jest wystarczająco daleko to dodaje +1 do cnt, następnie zwraca ten cnt
#zlożoność czasowa: nlogn
from kol1testy import runtests

def ogrodzenie(M, D, T):
  n = len(T)
  def quick_sort(A, p, r):
    if p < r:
      q = partition(A, p, r)
      quick_sort(A, p, q - 1)
      quick_sort(A, q + 1, r)

  def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
      if A[j] <= pivot:
        i += 1
        A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

  quick_sort(T, 0, len(T) - 1)


  cnt = 0
  if T[n-1] - T[0] < D:
    return 0
  for i in range(1,n):
    if T[i]-T[i-1]>D:
      cnt += 1
  return cnt




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )
