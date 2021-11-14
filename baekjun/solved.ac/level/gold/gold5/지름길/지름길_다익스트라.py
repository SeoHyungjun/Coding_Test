import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
li = []
for _ in range(n):
    st, en, length = map(int, input().split())
    if en <= m and en - st > length:
        li.append((st, en, length))

distance = [i for i in range(m+1)]

for i in range(m+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1] + 1)

    delete_index = []
    for j in range(len(li)):
        #st, en, length = li[j]
        if li[j][0] == i:
            delete_index.append(j)
            distance[li[j][1]] = min(distance[li[j][1]], distance[li[j][0]] + li[j][2])
            
    for j in sorted(delete_index, reverse=True):
        del li[j]

print(distance[m])