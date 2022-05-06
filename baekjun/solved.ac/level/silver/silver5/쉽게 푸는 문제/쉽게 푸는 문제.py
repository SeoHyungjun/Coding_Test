import sys

A, B = map(int, sys.stdin.readline().split())

arr = []
for i in range(50):
    for j in range(i):
        arr.append(i)

for i in range(1, 1200):
    arr[i] += arr[i-1]

if A == 1:
    minus_sum = 0
else:
    minus_sum = arr[A-2]
print(arr[B-1] - minus_sum)