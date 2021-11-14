import sys
import heapq

N = int(sys.stdin.readline())
board = {}

for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    i = data[0]-1
    data = data[1:-1]

    board[i] = []
    for j in range(0, len(data), 2):
        board[i].append((data[j]-1, data[j+1]))

def find_far(i):
    dij = [0] * N
    visit = [False] * N
    visit[i] = True
    queue = []
    heapq.heappush(queue, (0, 0, i))

    while queue:
        _, sum_cost, next = heapq.heappop(queue)

        for index, cost in board[next]:
            if (not visit[index]) and sum_cost + cost > dij[index]:
                dij[index] = sum_cost + cost
                visit[index] = True
                heapq.heappush(queue, (-1*dij[index], dij[index], index))

    #answer = max(max(dij), answer)
    return (dij.index(max(dij)), max(dij))

print(find_far(find_far(1)[0])[1])