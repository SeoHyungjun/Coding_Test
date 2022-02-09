import sys

while True:
    X = float(sys.stdin.readline())
    
    if X == -1:
        break

    Y = X*0.167
    print("Objects weighing %.2f on Earth will weigh %.2f on the moon."%(X, Y))