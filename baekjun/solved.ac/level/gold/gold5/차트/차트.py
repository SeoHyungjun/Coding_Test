import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

visit = set()
answer = 0
for per in permutations(arr):
    if per in visit:
        continue
    visit.add(per)
    tmp_answer = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            tmp += per[(i+j)%N]
            if tmp > 50:
                break
            elif tmp == 50:
                tmp_answer += 1
                break

    answer = max(answer, tmp_answer//2)

print(answer)