import sys

def findLeaf(index):
    numchildren = 0

    if deleteNode in tree[index]:
        del tree[index][tree[index].index(deleteNode)]

    if not tree[index]:
        return 1

    for child in tree[index]:
        numchildren += findLeaf(child)

    return numchildren

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
deleteNode = int(sys.stdin.readline())
tree = {i : [] for i in range(-1, N)}

for i in range(N):
    if arr[i] == -1:
        root = i
    tree[arr[i]].append(i)

if deleteNode == root:
    print(0)
else:
    print(findLeaf(-1))