# 2021-03-28 17:00 -> 
import heapq
import sys
input = sys.stdin.readline

answer = []

n, m = map(int, input().split())
peoples = [[ float('inf') if i != j else 0 for i in range(n)] for j in range(n) ]

for _ in range(m):
    a, b = map(int, input().split())
    peoples[a-1][b-1] = 1
    peoples[b-1][a-1] = 1

for i in range(n):
    distances = [float('inf')] * n
    distances[i] = 0

    queue = []
    heapq.heappush(queue, (0, i))

    while queue:
        cur_distance, cur_people = heapq.heappop(queue)

        for j in range(n):
            if cur_distance + peoples[cur_people][j] < distances[j]:
                distances[j] = cur_distance + peoples[cur_people][j]
                heapq.heappush(queue, (distances[j], j))

    answer.append((i+1, sum(distances)))

answer.sort(key = lambda x : (x[1], x[0]))
print(answer[0][0])