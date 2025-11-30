#trzeba przerobić
def L(T, h):
    n = len(T)
    s = 0
    for i in range(n):
        if T[i][0] <= h:
            s+= T[i][0] - T[i][1]
        elif h > T[i][1]:
            s += h - T[i][1]

    return s

def h(T, l):
    n = len(T)
    a = 0
    b = max(T)[0]
    eps = 10e-10
    while b - a > eps:
        sr = (a+b)/2
        if L(T, sr) > l:
            b = sr
        else:
            a = sr
    return sr


