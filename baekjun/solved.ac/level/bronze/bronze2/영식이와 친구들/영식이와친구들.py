import sys

N, M, L = map(int, sys.stdin.readline().split())

people = [0]*N
ball = 0
answer = 0

while True:
    people[ball] += 1
    if people[ball] == M:
        break

    if people[ball] % 2 != 0:
        ball = (ball + L) % N
    else:
        ball = (N + ball - L) % N

    answer += 1

print(answer)
