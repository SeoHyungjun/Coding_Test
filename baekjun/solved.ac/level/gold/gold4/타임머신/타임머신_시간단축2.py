import sys
input = sys.stdin.readline

N, M = map(int,input().split())
adjList = [[] for _ in range(N)]
INF = 2147483647
dist = [INF] * (N)
dist[0] = 0
isPossible = True

for _ in range(M):
    a,b,c = map(int,input().split())
    adjList[a-1].append((c,b-1))

for repeat in range(N):
    for i in range(N):
        for wei, vec in adjList[i]:
            if dist[i] != INF and dist[vec] > dist[i] + wei:
                dist[vec] = dist[i] + wei
                if repeat == N-1:
                    isPossible = False

if not isPossible:
    print(-1)
else:
    for d in dist[1:]:
        print(d if d !=INF else -1)
