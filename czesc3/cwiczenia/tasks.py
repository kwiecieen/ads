def tasks(T):
    T.sort(key=lambda task: task[1], reverse=True)
    limit = max(task[0] for task in T)
    slots = [False] * limit
    result = []
    for task in T:
        for slot in range(task[0]-1,-1,-1):
            if not slots[slot]:
                slots[slot] = True
                result.append(task)
                break
    return result[::-1]

T = [[1, 20], [3, 45], [2, 30], [2, 25], [1, 15]]
print(tasks(T))