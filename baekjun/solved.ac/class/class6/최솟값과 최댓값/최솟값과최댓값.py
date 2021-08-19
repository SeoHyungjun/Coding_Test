import sys
import math

def init_min(start, end, index):
    if start == end:
        min_tree[index] = arr[start]
    else:
        mid = (start +  end) // 2
        min_tree[index] = min(init_min(start, mid, index*2), init_min(mid+1, end, index*2 + 1))
    return min_tree[index]

def find_min(start, end, index):
    if left > end or right < start:
        return float('inf')
    if left <= start and end <= right:
        return min_tree[index]

    mid = (start + end) // 2
    return min(find_min(start, mid, index*2), find_min(mid+1, end, index*2 + 1))

def init_max(start, end, index):
    if start == end:
        max_tree[index] = arr[start]
    else:
        mid = (start +  end) // 2
        max_tree[index] = max(init_max(start, mid, index*2), init_max(mid+1, end, index*2 + 1))
    return max_tree[index]

def find_max(start, end, index):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return max_tree[index]
    
    mid = (start + end) // 2
    return max(find_max(start, mid, index*2), find_max(mid+1, end, index*2 + 1))

N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]

tree_size = (1 << (int(math.ceil(math.log2(N))) + 1))
min_tree = [float('inf')] * tree_size
max_tree = [0] * tree_size
init_min(0, N-1, 1)
init_max(0, N-1, 1)

for _ in range(M):
    left, right = map(int, sys.stdin.readline().split())
    left, right = left - 1, right - 1
    print(find_min(0, N-1, 1), find_max(0, N-1, 1))