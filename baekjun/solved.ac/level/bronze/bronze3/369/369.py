import sys

N = int(sys.stdin.readline())

answer = 0
for i in range(1, N+1):
    answer += str(i).count('3') + str(i).count('6') + str(i).count('9')

print(answer)