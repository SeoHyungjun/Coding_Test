import sys

_ = sys.stdin.readline().split()
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

print(len(A^B))