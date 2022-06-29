import sys

N = sys.stdin.readline().rstrip()

answer = 0
for i in range(1, len(N)):
    answer += 9*10**(i-1)*i
answer += (int(N)-10**(len(N)-1)+1)*len(N)

print(answer)