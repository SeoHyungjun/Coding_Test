import sys
import math

def update(start, end, node, index, val):
    if index < start or index > end: return
    tree[node] += val
    if start == end: return
    mid = (start + end) >> 1
    update(start, mid, node*2, index, val)
    update(mid + 1, end, node*2 + 1, index, val)

def query(start, end, node, left, right):
    if end < left or right < start: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start + end) >> 1
    return query(start, mid, node*2, left, right) + query(mid + 1, end, node*2 + 1, left, right)


N, Q = map(int, sys.stdin.readline().split())
depth = math.ceil(math.log2(N) + 1)
tree = [0] * pow(2, depth)

for _ in range(Q):
    com, p, q = map(int, sys.stdin.readline().split())

    if com & 1: update(1, N, 1, p, q)
    else: print(query(1, N, 1, p, q))