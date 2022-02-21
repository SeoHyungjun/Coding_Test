import sys

answer = 0
for i in range(8):
    line = list(sys.stdin.readline())
    for j in range(8):
        if (j + i)%2 == 0 and line[j] == 'F':
            answer += 1

print(answer)