import sys
INF = float('inf')

def tsp(cur, visited):
    # 모두 방문했을 시
    if visited == (1<<N) - 1:
        # 마지막 방문 도시에서 시작점(0)으로 돌아가는 길이 있다면
        if graph[cur][0]:
            return graph[cur][0]
        # 돌아갈 길이 없다면
        else:
            return INF

    # 모두 방문하지 않았을 때
    # 이미 한번 체크했던 경우라면 -> 결과값이 저장되어있으므로 바로 return
    if bitmask[cur][visited] != -1:
        return bitmask[cur][visited]

    bitmask[cur][visited] = INF
    for i in range(N):
        # i를 이미 방문했다면
        if visited & (1 << i):
            continue
        # i를 방문할 수 없다면
        if not graph[cur][i]:
            continue
        bitmask[cur][visited] = min(bitmask[cur][visited], tsp(i, visited | (1<<i)) + graph[cur][i])
    
    return bitmask[cur][visited]

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bitmask = [[-1] * (1<<N) for _ in range(N)]

print(tsp(0,1))