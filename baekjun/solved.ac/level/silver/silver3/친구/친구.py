import sys

N = int(sys.stdin.readline())
friend = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k: continue

            if friend[j][k] == 'Y' or (friend[j][i] == 'Y' and friend[i][k] == 'Y'):
                visit[j][k] = 1

answer = 0
for i in visit:
    answer = max(answer, sum(i))

print(answer)