#odtwarzanue/wypisywanie najkrotszej sciezki na podstawie tablicy parentow

def restore(parents, t):
    path = [t]
    while parents[t] != None:
        path.append(parents[t])
        t = parents[t]
    return path.reverse()
