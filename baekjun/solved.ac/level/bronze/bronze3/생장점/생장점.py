import sys

while True:
    arr = list(map(int, sys.stdin.readline().split()))

    if len(arr) == 1 and arr[0] == 0:
        break

    age, arr = arr[0], arr[1:]
    cur_branch = 1

    for i in range(age):
        cur_branch *= arr[2*i]
        cur_branch -= arr[2*i+1]

    print(cur_branch)