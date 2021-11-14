import sys
import heapq
INF = int(1e9)

TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())

    gr = []

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        gr.append((S-1, E-1, T))
        gr.append((E-1, S-1, T))

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        gr.append((S-1, E-1, -T))

    distance = [INF] * N
    distance[0] = 0

    state = False
    for i in range(N):
        for s, e, t in gr:
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                if i == N-1:
                    state = True

    print('YES' if state else 'NO')