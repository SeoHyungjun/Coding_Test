import sys

N = int(sys.stdin.readline())

first = 0
candys = []
for i in range(N):
    candys.append(int(sys.stdin.readline()))

    if i % 2 == 0:
        first += candys[-1]
    else:
        first -= candys[-1]

answer = [first // 2]
for i in range(N-1):
    answer.append(candys[i] - answer[i])

print(*answer, sep='\n')