import sys
INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
gr = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    gr.append((A-1,B-1,C))

distance = [INF] * N
distance[0] = 0
state = False

for i in range(N):
    for s, e, c in gr:
        if distance[s] != INF and distance[e] > distance[s] + c:
            distance[e] = distance[s] + c
            if i == N-1:
                state = True

if state:
    print(-1)
else:
    for i in distance[1:]:
        print(-1 if i == INF else i)