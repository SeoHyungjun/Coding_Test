import sys
import math
from collections import defaultdict

def update(start, end, node, index):
    if index < start or index > end: return
    if start == end: 
        tree[node] += 1
        return
    mid = (start + end) >> 1
    update(start, mid, node * 2, index)
    update(mid + 1, end, node * 2 + 1, index)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(start, end, node, left, right):
    if end < left or right < start: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start + end) >> 1
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
pos = defaultdict(int)
index = sorted(arr)
for i in range(N):
    pos[arr[i]] = i + 1

depth = math.ceil(math.log2(N) + 1)
tree = [0] * (1 << depth)
answer = 0

for i in index:
    cur = pos[i]
    answer += query(1, N, 1, cur + 1, N)
    update(1, N, 1, cur)

print(answer)