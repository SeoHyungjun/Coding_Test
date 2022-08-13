import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cur = sys.stdin.readline().rstrip()
    print(cur[0]+cur[-1])