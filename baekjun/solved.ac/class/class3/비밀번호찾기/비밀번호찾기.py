import sys

N, M = map(int, sys.stdin.readline().split())

site = {}

for _ in range(N):
    s, pw = sys.stdin.readline().rstrip().split()
    site[s] = pw

for _ in range(M):
    print(site[sys.stdin.readline().rstrip()])