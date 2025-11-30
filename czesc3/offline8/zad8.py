from zad8testy import runtests

def ice_cream( T ):
    def counting_sort_for_radix(arr, place):
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # dla cyfr 0-9

        for i in range(n):
            index = (arr[i] // place) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // place) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    def radix_sort(arr):
        max_val = max(arr)
        place = 1
        while max_val // place > 0:
            counting_sort_for_radix(arr, place)
            place *= 10
    radix_sort(T)
    i = len(T)-1
    melt = 0
    res = 0
    while T[i]-melt>0 and i>=0:
        res += (T[i] - melt)
        melt +=1
        i -= 1

    return res



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
