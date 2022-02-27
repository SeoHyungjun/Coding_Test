import sys

A, B = sys.stdin.readline().split()

print(bin(int(A, 2)+int(B, 2)).replace('0b', ''))