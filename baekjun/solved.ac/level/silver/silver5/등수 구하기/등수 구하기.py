import sys

N, point, P = map(int, sys.stdin.readline().split())
if N == 0:
    print(1)
else:
    arr = list(map(int, sys.stdin.readline().split()))

    if N == P and arr[-1] >= point:
        print(-1)
    else:
        rank = 1
        for i in range(N):
            if arr[i] > point:
                rank += 1
            else:
                break

        print(rank)