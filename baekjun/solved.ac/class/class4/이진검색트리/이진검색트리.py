import sys
from bisect import bisect_left
sys.setrecursionlimit(int(1e6))

pre = []

def find_post(st, en):
    if st > en:
        return
    
    root = pre[st]
    right = bisect_left(pre, root, st+1, en+1)
    
    find_post(st+1, right-1)
    find_post(right, en)
    print(root)
    

for _ in range(10000):
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

find_post(0, len(pre)-1)