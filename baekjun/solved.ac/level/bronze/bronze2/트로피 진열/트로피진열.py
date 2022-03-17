import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

left_top, right_top = 0, 0
left_anser, right_answer = 0, 0
for i in range(N):
    if arr[i] > left_top:
        left_anser += 1
        left_top = arr[i]

    if arr[N-1-i] > right_top:
        right_answer += 1
        right_top = arr[N-1-i]

print(left_anser, right_answer, sep = '\n')