import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    sum_arr = sum([int(sys.stdin.readline()) for _ in range(N)])

    if sum_arr > 0:
        print('+')
    elif sum_arr == 0:
        print(0)
    else:
        print('-')