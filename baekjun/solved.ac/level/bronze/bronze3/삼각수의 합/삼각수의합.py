import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    answer = 0
    for i in range(1, N+1):
        answer += i * (i+1)*(i+2)/2

    print(int(answer))