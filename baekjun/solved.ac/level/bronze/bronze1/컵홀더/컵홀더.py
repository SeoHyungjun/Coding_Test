import sys

N = int(sys.stdin.readline())
chair = sys.stdin.readline().rstrip()

answer = 0
chair = chair.replace('S', ' S ').replace('LL', ' S ').split()

print(min(N, len(chair) + 1))