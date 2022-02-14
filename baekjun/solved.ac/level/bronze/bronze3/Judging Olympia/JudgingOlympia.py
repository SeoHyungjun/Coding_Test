import sys

while True:
    arr = sorted(list(map(int, sys.stdin.readline().split())))

    if sum(arr) == 0:
        break

    answer = sum(arr[1:-1])/4
    answer_int = sum(arr[1:-1])//4

    if answer == answer_int:
        print(answer_int)
    else:
        print(answer)