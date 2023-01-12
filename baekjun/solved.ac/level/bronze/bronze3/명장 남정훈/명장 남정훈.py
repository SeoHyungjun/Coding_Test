import sys

L, R, A = map(int, sys.stdin.readline().split())
print(min(L+A,R+A,L+R+A>>1)*2)