import sys

N = int(sys.stdin.readline())
Q1 = Q2 = Q3 = Q4 = AXIS = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1

print("Q1: %d" %(Q1))
print("Q2: %d" %(Q2))
print("Q3: %d" %(Q3))
print("Q4: %d" %(Q4))
print("AXIS: %d" %(AXIS))