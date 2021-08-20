import sys
import math

def init_tree(start, end, index):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        tree[index] = init_tree(start, mid, index*2) + init_tree(mid+1, end, index*2 + 1)
    return tree[index]

def find_sum(start, end, index):
    if left - 1 > end or right - 1 < start:
        return 0
    if left - 1 <= start and end <= right - 1:
        return tree[index]

    mid = (start + end) // 2
    return find_sum(start, mid, index*2) + find_sum(mid+1, end, index*2 + 1)

def update_tree(start, end, index, where, diff):
    if where < start or end < where:
        return 
    
    tree[index] += diff
    if start != end:
        mid = (start + end) // 2
        update_tree(start, mid, index*2, where, diff)
        update_tree(mid+1, end, index*2 + 1, where, diff)

N, M, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
init_tree(0, N-1, 1)

for _ in range(M+K):
    com, left, right = map(int, sys.stdin.readline().split())
    if com == 1:
        diff = right - arr[left - 1]
        arr[left-1] = right
        update_tree(0, N-1, 1, left-1, diff)
    else:
        print(find_sum(0, N-1, 1))