import sys
import math

def min_index(a, b):
    if a == float('inf'):
        return b
    if b == float('inf'):
        return a

    if arr[a] == arr[b]:
        return a if a < b else b
    return a if arr[a] < arr[b] else b

def find_min(start, end, index, left, right):
    if left > end or right < start:
        return float('inf')

    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return min_index(find_min(start, mid, 2*index, left, right), find_min(mid+1, end, 2*index+1, left, right))

def update_tree(start, end, index, change_index):
    if start <= change_index and change_index <= end and start != end:
        mid = (start + end) // 2
        tree[index] = min_index(update_tree(start, mid, 2*index, change_index), update_tree(mid+1, end, 2*index+1, change_index))
    return tree[index]

def init_tree(start, end, index):
    if start == end:
        tree[index] = start
    else:
        mid = (start + end) // 2
        tree[index] = min_index(init_tree(start, mid, 2*index), init_tree(mid+1, end, 2*index+1))
    return tree[index]

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
tree = [float('inf')] * (1 << (int(math.ceil(math.log2(N))) + 1))
init_tree(0, N-1, 1)

M = int(sys.stdin.readline())
for _ in range(M):
    com, a, b = map(int, sys.stdin.readline().split())
    if com == 1:
        arr[a-1] = b
        update_tree(0, N-1, 1, a-1)
    else:
        print(find_min(0, N-1, 1, a-1, b-1) + 1)