import sys

num = list(map(int, sys.stdin.readline().rstrip('\n')))
num.sort(reverse=True)

for i in range(len(num)):
    print(num[i], end = '')
