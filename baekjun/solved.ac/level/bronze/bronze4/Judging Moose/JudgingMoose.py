import sys

L, R = map(int, sys.stdin.readline().split())

if L == 0 and R == 0:
    print('Not a moose')
elif L == R:
    print('Even %d'%(L*2))
else:
    print('Odd %d'%(max(L, R)*2))