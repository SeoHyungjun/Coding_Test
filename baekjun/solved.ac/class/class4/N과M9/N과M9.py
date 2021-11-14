import sys

def find(index):
    global before
    if len(tmp) == M:
        print(*tmp)
        return
    
    before = ''
    for i in range(len(arr)):
        if not visited[i] and before != arr[i]:
            tmp.append(arr[i])
            visited[i] = True
            find(i)
            tmp.pop()
            visited[i] = False
            before = arr[i]

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
tmp = []
visited = [False] * N
find(0)