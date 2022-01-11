import sys

length = sorted(list(map(int, sys.stdin.readline().split())))

print(length[0]*length[2])