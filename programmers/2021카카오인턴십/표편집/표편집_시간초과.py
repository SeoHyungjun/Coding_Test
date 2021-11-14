def solution(n, k, cmd):
    status = ['O'] * n
    stack = []
    
    for c in cmd:
        if c[0] == 'U':
            for i in range(int(c[2:])):
                k -= 1
                while status[k] == 'X':
                    k -= 1

        elif c[0] == 'D':
            for i in range(int(c[2:])):
                k += 1
                while status[k] == 'X':
                    k += 1

        elif c[0] == 'C':
            stack.append(k)
            status[k] = 'X'
            prevk = k
            for i in range(k+1, n):
                if status[i] == 'O':
                    k = i
                    break
            if prevk == k:
                while status[k] == 'X':
                        k -= 1

        elif c[0] == 'Z':
            cur = stack.pop()
            status[cur] = 'O'
            if cur < k:
                while status[k] == 'X':
                    k += 1

    return ''.join(status)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))