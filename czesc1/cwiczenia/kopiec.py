#drzewo kompletne
#wzor na synów: n=indeks ojca ; left = 2n+1 ; right = 2n+2 !!!dla indeksow od 0 | ojciec = (i-1)//2
#jak na indeksie 0 przechowamy dlugosc kopca, to: left = 2n ; right = 2n+1 | ojciec = i//2


def insert(T, ne):
    n = len(T)
    T[0] += 1
    assert T[0] != 1
    ind = T[0]
    T[ind] = ne
    while ind > 1 and T[ind] > T[ind//2]:
        T[ind], T[ind//2] = T[ind//2], T[ind]
        ind = ind//2

T = [5, 40, 25, 10, 7, 4, 26]
insert(T, 31)
print(T)

