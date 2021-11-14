import sys
from bisect import bisect_left, bisect, bisect_right

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

N, M, K = map(int, sys.stdin.readline().split())
minsoo = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(len(minsoo))]
chulsoo = list(map(int, sys.stdin.readline().split()))

minsoo.sort()
for card in chulsoo:
    index = bisect_left(minsoo, card+1)
    parent_index = find(index)
    print(minsoo[parent_index])
    parent[parent_index] += 1