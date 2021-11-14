def solution(n, k, cmd):
    linkedList = {i:[i-1, i+1] for i in range(n)}
    status = ['O'] * n
    deletedStack = []

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linkedList[k][1]

        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linkedList[k][0]

        elif c[0] == 'C':
            prev, next = linkedList[k]
            deletedStack.append((prev, next, k))
            status[k] = 'X'

            if prev > -1:
                linkedList[prev][1] = next 
            if next < n:
                linkedList[next][0] = prev

            k = next if next < n else prev

        elif c[0] == 'Z':
            prev, next, cur = deletedStack.pop()
            status[cur] = 'O'

            if prev > -1:
                linkedList[prev][1] = cur
            if next < n:
                linkedList[next][0] = cur

    return ''.join(status)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))