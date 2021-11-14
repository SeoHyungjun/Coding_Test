import sys

X,Y,D,T=map(int, sys.stdin.readline().split())

distance = (X**2 + Y**2)**0.5

if distance >= D:
    print(min(distance, T * (distance//D) + (distance%D), T*(distance//D + 1)))
else:
    print(min(distance, T*2, T * (distance//D + 1) + (D - distance%D)))