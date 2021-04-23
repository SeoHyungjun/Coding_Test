# pre -> root lc rc
# in -> lc root rc
# post -> lc rc root

import sys
sys.setrecursionlimit(1000000000)

def preorder(s_in, e_in, s_po, e_po):
    if s_po <= e_po:
        root = postorder[e_po]
        print(root, end = ' ')
        index = inorder_index[root]
        preorder(s_in, index-1, s_po, s_po + index - 1 - s_in)
        preorder(index + 1, e_in, s_po + index - s_in, e_po - 1)

N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().rstrip().split()))
inorder_index = [0] * (N+1)
for i in range(N):
    inorder_index[inorder[i]] = i
postorder = list(map(int, sys.stdin.readline().rstrip().split()))

preorder(0, N-1, 0, N-1)