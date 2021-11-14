import sys

n = int(sys.stdin.readline())
f_li = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
s_li = list(map(int, sys.stdin.readline().split()))

for s in s_li:
    if s in f_li:
        print('1')
    else:
        print('0')