import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    global team, answer
    visited[n] = True
    next_student = arr[n] -1
    team.append(n)

    if not visited[next_student]:
        dfs(next_student)
    elif next_student in team:
        answer += len(team) - team.index(next_student)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    visited = [False] * N
    answer = 0

    for i in range(N):
        if not visited[i]:
            team = []
            dfs(i)
    print(N-answer)