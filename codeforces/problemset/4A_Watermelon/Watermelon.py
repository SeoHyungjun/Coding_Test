import sys

def is_Even(weight):
    if weight > 2 and weight % 2 == 0:
        return 'YES'
    return 'NO'

W = int(sys.stdin.readline())

print(is_Even(W))