import sys

arr = [False]*31
for _ in range(28):
    num = int(sys.stdin.readline())
    arr[num] = True
    
for i in range(1, 31):
    if arr[i]:
        continue
    print(i)