import sys

print(bin(int(sys.stdin.readline().rstrip(), 2) * int(sys.stdin.readline().rstrip(), 2))[2:])