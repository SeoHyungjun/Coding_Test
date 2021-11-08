import sys

day = int(sys.stdin.readline())
cars = list(map(int, sys.stdin.readline().split()))

print(len([x for x in cars if x == day]))