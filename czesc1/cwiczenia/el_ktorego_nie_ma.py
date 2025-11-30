def naj(A):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        s = (r + l)//2
        if  s == A[s]:
            l = s + 1
        else:
            r = s - 1
    return l

A = [0,1,2,3,7,8]
print(naj(A))