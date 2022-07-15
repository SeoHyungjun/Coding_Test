import sys

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
T = int(sys.stdin.readline())
for _ in range(T):
    s, n = map(int, sys.stdin.readline().split())

    if s == 1: # 남학생
        for cur_n in range(n, N+1, n):
            switch[cur_n - 1] = (switch[cur_n - 1] + 1) % 2
            cur_n *= 2

    else: # 여학생
        switch[n-1] = (switch[n-1] + 1) % 2
        start, end = n-2, n

        while start >= 0 and end < N:
            if switch[start] != switch[end]:
                break
            switch[start] = switch[end] = (switch[start] + 1) % 2
            start -= 1
            end += 1

cnt = 0
for i in switch:
    print(i, end = ' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0