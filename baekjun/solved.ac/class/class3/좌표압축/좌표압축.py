import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
set_arr = sorted(set(arr))

dic = {}
for i in range(len(set_arr)):
    dic[set_arr[i]] = i

for i in arr:
    print(dic[i], end = ' ')