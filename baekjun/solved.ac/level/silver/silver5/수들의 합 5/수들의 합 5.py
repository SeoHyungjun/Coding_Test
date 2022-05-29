import sys

N = int(sys.stdin.readline())

a, b, sum = 1, 1, 1
answer = 0

while a <= b <= N:
    if sum == N:
        answer += 1
        b += 1
        sum += b - a
        a += 1
    elif sum > N:
        sum -= a
        a += 1
    else:
        b += 1
        sum += b

print(answer)