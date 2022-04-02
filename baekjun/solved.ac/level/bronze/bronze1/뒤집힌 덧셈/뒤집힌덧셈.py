import sys

def Rev(X):
    X = str(X)
    return int(X[::-1])

X, Y = map(int, sys.stdin.readline().split())

print(Rev(Rev(X) + Rev(Y)))