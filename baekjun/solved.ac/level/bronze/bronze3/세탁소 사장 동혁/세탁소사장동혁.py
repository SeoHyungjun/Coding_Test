import sys

cents = [25, 10, 5, 1]
T = int(sys.stdin.readline())

for _ in range(T):
    C = int(sys.stdin.readline())

    answer = [0, 0, 0, 0]
    for i, cent in enumerate(cents):
        answer[i] = C//cent
        C %= cent

    print(*answer)