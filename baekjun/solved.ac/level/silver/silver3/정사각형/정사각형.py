import sys

def distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

T = int(sys.stdin.readline())
for _ in range(T):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

    length = []
    for i in range(4):
        for j in range(i+1, 4):
            length.append(distance(arr[i], arr[j]))
    length.sort()

    print(1) if len(set(length[:4])) == 1 and len(set(length[4:])) == 1 else print(0)