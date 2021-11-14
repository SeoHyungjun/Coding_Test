import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key = lambda x : x[0])

tmp = []
label = []
for i in range(len(arr)):
    if not tmp or arr[i][1] > tmp[-1]:
        where = len(tmp)
        tmp.append(arr[i][1])

    elif arr[i][1] < tmp[-1]:
        where = bisect_left(tmp, arr[i][1])
        tmp[where] = arr[i][1]

    else:
        continue

    label.append(where)

last = max(label)
not_answer = set()
answer = set()
for i in range(N-1, -1, -1):
    answer.add(arr[i][0])
    if label[i] == last:
        not_answer.add(arr[i][0])
        last -= 1

answer = answer.difference(not_answer)
print(len(answer))
print(*answer, sep = '\n')