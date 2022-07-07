import sys

N, Kim, Im = map(int, sys.stdin.readline().split())
count = 0
while Kim != Im:
    Kim -= Kim // 2
    Im -= Im // 2
    count += 1
print(count)