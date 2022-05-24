import sys

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    if num % 2 == 0:
        print('NO')
        continue

    answer = 'YES'
    for i in range(3, 10**6 + 1, 2):
        if num % i == 0:
            answer = 'NO'
            break

    print(answer)