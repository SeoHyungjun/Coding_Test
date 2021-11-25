import sys

ball = 1
for _ in range(int(sys.stdin.readline())):
    X, Y = map(int, sys.stdin.readline().split())

    if X == ball:
        ball = Y
    elif Y == ball:
        ball = X
        
print(ball)