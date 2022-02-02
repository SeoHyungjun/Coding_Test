import sys

N = int(sys.stdin.readline())

while True:
    num = int(sys.stdin.readline())

    if num == 0:
        break

    if num % N == 0:
        print('%d is a multiple of %d.'%(num, N))
    else:
        print('%d is NOT a multiple of %d.'%(num, N))