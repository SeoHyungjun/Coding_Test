import sys

A, B = map(int, sys.stdin.readline().split())
A_set = set(list(map(int, sys.stdin.readline().split())))
B_set = set(list(map(int, sys.stdin.readline().split())))

diff = A_set.difference(B_set)
print(len(diff))
if diff:
    print(*sorted(diff))