import sys

x, k = map(int, sys.stdin.readline().split())
x = x*1000
k = k*1000

answer = 0

# k가 1번째 눈사람일 경우
if 7*k <= x:
    answer = 7*k

# k가 2번째 눈사람일 경우
elif k//2 % 2 == 0 and k//2 + 3*k <= x:
    answer = k//2 + 3*k

# k가 3번째 눈사람일 경우
elif k//4 %2 == 0 and k//2 % 2 == 0 and k//4 + k//2 + k <= x:
    answer = k//4 + k//2 + k

print(answer)