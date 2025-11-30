def find_sum(T, s):
    n = len(T)
    L = 0
    P = n - 1
    while L < P:
        if T[L] + T[P] > s:
            P -= 1
        elif T[L] + T[P] < s:
            L += 1
        else:
            return True
    return False

T = [2, 3, 4, 5, 7, 8]
print(find_sum(T, 16))