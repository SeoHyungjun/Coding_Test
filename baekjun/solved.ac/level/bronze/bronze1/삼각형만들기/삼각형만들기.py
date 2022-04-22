import sys

N = int(sys.stdin.readline())

answer = 0
if N == 1 or N == 2 or N == 4:
    print(answer)
else:
    for c in range(1, N+1):
        if N <= 3*c and 2*c < N:
            answer += c - (N-c-1)//2

    print(answer)

"""
삼각형의 조건
세 변을 a, b, c라고 했을 때

a + b + c = N
a + b > c (가장 긴 변의 길이가 나머지 두 변의 합보다 작아야 한다)

c의 범위는 
a <= c, b <= c
-> a + b <= 2c
-> a + b + c <= 3c

a + b > c
a + b + c > 2c
N > 2c

즉, N/3 <= C < N/2


각 c에 대해서 b의 범위 계산가능 -> a도 결정
a <= b <= c
a = N - b - c <= b <= c
(N-c)/2 <= b <= c
"""