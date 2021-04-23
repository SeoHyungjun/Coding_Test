import sys

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    r, lc, rc = sys.stdin.readline().split()
    tree[r] = (lc, rc)

def preorder(start):
    lc, rc = tree[start]
    print(start, end = '')
    if lc != '.':
        preorder(lc)
    if rc != '.':
        preorder(rc)

def inorder(start):
    lc, rc = tree[start]
    if lc != '.':
        inorder(lc)
    print(start, end = '')
    if rc != '.':
        inorder(rc)

def postorder(start):
    lc, rc = tree[start]
    if lc != '.':
        postorder(lc)
    if rc != '.':
        postorder(rc)
    print(start, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')