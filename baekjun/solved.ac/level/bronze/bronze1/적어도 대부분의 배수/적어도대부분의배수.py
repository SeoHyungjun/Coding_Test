import sys

arr = list(map(int, sys.stdin.readline().split()))
answer = 1

while True:
    cnt = 0

    for i in arr:
        if answer % i == 0:
            cnt += 1

    if cnt >= 3:
        print(answer)
        break

    answer += 1