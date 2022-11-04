import sys

N = int(sys.stdin.readline())

print("CY" if N % 5 == 0 or N % 5 == 2 else "SK")