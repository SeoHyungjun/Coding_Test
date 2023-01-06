import sys

N = int(sys.stdin.readline())
P = int(sys.stdin.readline())

answer = P
if N >= 20:
    answer = min(answer, int(P * 0.75))
if N >= 15:
    answer = min(answer, P - 2000)
if N >= 10:
    answer = min(answer, int(P * 0.9))
if N >= 5:
    answer = min(answer, P - 500)
    
print(answer if answer > 0 else 0)