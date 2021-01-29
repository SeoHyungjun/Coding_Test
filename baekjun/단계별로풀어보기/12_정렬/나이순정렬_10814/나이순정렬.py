import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().split())

arr.sort(key = lambda x : int(x[0]))

for age, name in arr:
    print(age, name)