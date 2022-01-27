import sys

B, W = map(int, sys.stdin.readline().split())

answer = "Impossible"

for i in range(1, 10001):
    half = (i**2)//2
    other = i**2 - half

    if (B >= half and W >= other) or (B >= other and W >= half):
        answer = i
        continue
    break

print(answer)