import sys
sys.setrecursionlimit(10**9)

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(x, y, depth, p):
    if depth >= N:
        return p

    result = 0
    visit.add((x, y))

    for i in range(4):
        if arr[i] == 0:
            continue

        if (x+direction[i][0], y+direction[i][1]) not in visit:
            result += dfs(x+direction[i][0], y+direction[i][1], depth+1, p*arr[i])

    visit.remove((x, y))
    return result

N, a, b, c, d = map(int, sys.stdin.readline().split())
arr = [a/100, b/100, c/100, d/100]
visit = set()

answer = dfs(14, 14, 0, 1.0)

print(answer)