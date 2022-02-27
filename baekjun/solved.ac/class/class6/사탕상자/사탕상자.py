import sys
import math
MAX_CANDY = 1000000

def update(node, start, end, index, diff):
    global tree
    
    if not (start <= index and index <= end):
        return

    tree[node] += diff
    if (start != end):
        mid = (start + end) // 2
        update(node*2,     start,   mid, index, diff)
        update(node*2 + 1, mid + 1, end, index, diff)

def query(node, start, end, k):
    global tree
    
    if start == end:
        #print(start)
        return start

    mid = (start + end) // 2
    if node*2 <= tree_size and tree[node*2] >= k:
        return query(node*2, start, mid, k)
    
    k -= tree[node*2]
    if node*2 + 1 <= tree_size and tree[node*2 + 1] >= k:
        return query(node*2 + 1, mid + 1, end, k)

tree_depth = int(math.ceil(math.log2(MAX_CANDY))) + 1
tree_size = 1 << tree_depth
tree = [0] * tree_size

N = int(sys.stdin.readline())
for _ in range(N):
    com = list(map(int, sys.stdin.readline().split()))

    if com[0] == 1: # 사탕 빼기
        getIndex = query(1, 0, MAX_CANDY - 1, com[1])
        print(getIndex)
        update(1, 0, MAX_CANDY - 1, getIndex, -1)

    else: # com[0] == 2, 사탕 넣기
        update(1, 0, MAX_CANDY - 1, com[1], com[2])