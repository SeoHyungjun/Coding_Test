import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)

answer = []
for i in range(N):
    index = sorted_arr.index(arr[i])
    answer.append(index)
    sorted_arr[index] = -1

print(*answer)