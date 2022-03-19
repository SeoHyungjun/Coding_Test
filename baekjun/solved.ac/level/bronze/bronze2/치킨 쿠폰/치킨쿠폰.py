import sys

while True:
    try:
        N, K = map(int, sys.stdin.readline().split())
        answer = N

        while N//K:
            answer += N//K
            N = N//K + N%K

        print(answer)
    except:
        break