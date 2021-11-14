# 시간 812ms
import sys
INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
gr = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    gr[A-1].append((B-1, C))

distance = [INF] * N
distance[0] = 0
state = False

for i in range(N):
    for s in range(N):
        for e, c in gr[s]:
            if distance[s] != INF and distance[e] > distance[s] + c:
                distance[e] = distance[s] + c
                if i == N-1:
                    state = True

if state:
    print(-1)
else:
    for i in distance[1:]:
        print(-1 if i == INF else i)