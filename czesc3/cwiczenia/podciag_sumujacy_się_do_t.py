# W problemie sumy podzbioru mamy dany ciąg liczb naturalnych A[0], ..., A[n - 1] oraz liczbę t.
# Należy stwierdzić czy istnieje podciąg sumujący się do t.

def is_there_sum(T, t, i = 0):
    n = len(T)
    if i >= n or t<0: return False
    if t == 0: return True
    return is_there_sum(T, t, i+1) or is_there_sum(T, t - T[i], i+1)


A = [1,4]
t = 3
print(is_there_sum(A, t, 0))
