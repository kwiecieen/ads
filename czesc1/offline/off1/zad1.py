from czesc1.offline.off1.zad1testy import runtests

def strong_string(T):
    n = len(T)
    maxi = 0
    max_lenght = 0
    for i in range(n):
        max_lenght = max(max_lenght, len(T[i]))
    buckets = [[]for i in range(max_lenght+1)]
    for s in T:
        buckets[len(s)].append(s)
    maxi = 0
    for bucket in buckets:
        cnt = []
        slowa = []
        if len(bucket) != 0:
            for s in bucket:
                r = s[::-1]
                if s == r:
                    if not s in slowa:
                        slowa.append(s)
                        cnt.append(0)
                    cnt[slowa.index(s)] += 1
                else:
                    if s<r:
                        if not s in slowa:
                            slowa.append(s)
                            cnt.append(0)
                        cnt[slowa.index(s)] += 1
                    else:
                        if not r in slowa:
                            slowa.append(r)
                            cnt.append(0)
                        cnt[slowa.index(r)] += 1
            maxi = max(maxi,max(cnt))



    return maxi








# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( strong_string, all_tests=False )
