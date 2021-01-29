import sys

num = list(map(int, sys.stdin.readline().rstrip('\n')))
num.sort(reverse=True)

print(num)
