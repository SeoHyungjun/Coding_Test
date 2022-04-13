import sys
import math

N = int(sys.stdin.readline())

if N <= 4:
    print(4)
else:
    length = math.ceil(N**0.5)

    if length * (length-1) >= N:
        print(2 * (length+length-3))
    else:
        print(4*(length-1))