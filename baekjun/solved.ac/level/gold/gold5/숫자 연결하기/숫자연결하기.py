import sys

N, K = map(int, sys.stdin.readline().split())

answer = 1
tmp = N
visit = set()

while True:
    if tmp % K == 0:
        break

    if tmp % K in visit:
        answer = -1
        break

    visit.add(tmp%K)
    tmp = int(str(tmp % K) + str(N))
    answer += 1

print(answer)