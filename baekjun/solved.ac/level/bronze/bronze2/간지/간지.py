import sys

N = int(sys.stdin.readline())

print("ABCDEFGHIJKL"[((N-1984)%60)%12] + str(((N-1984)%60)%10))