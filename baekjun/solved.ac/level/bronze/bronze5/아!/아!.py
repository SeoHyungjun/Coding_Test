import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

if len(a) >= len(b):
    print('go')
else:
    print('no')