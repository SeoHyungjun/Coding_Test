import sys

T = int(sys.stdin.readline())

for _ in range(T):
    _ = sys.stdin.readline()
    N = int(sys.stdin.readline())
    candy = [int(sys.stdin.readline()) for _ in range(N)]

    if sum(candy) % N == 0:
        print('YES')
    else:
        print('NO')