# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0,..., n-1. Dla każdego i € {0,...,n—1} znany jest zysk c_i, jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f(i) = maksymalna suma którą możemy uzyskać od A[o,..,i-1]
# f(i) = max { f(i - 1), f(i - 2) + A[i] } - albo nie ścinamy drzewa, albo ścinamy
# f(0) = 0
# f(1) = A[0]
# f(2) = max(A[1],f(1))