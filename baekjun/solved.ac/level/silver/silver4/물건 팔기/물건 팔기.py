import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = []
for price, _ in arr:
    tmp = 0
    for a, b in arr:
        if a < price or price - b <= 0:
            continue
        tmp += price - b
    
    answer.append([tmp, price])

answer.sort(key=lambda x:(-x[0], x[1]))
print(answer[0][1]) if answer[0][0] > 0 else print(0)