import sys

while True:
    try:
        N, S = map(int, sys.stdin.readline().split())
        print(S//(N+1))
    except:
        break