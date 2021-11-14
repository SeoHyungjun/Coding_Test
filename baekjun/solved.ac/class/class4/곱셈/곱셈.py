import sys

A, B, C = map(int, sys.stdin.readline().split())

def div(A, B):
    if B == 1:
        return A%C

    tmp = div(A, B//2)
    # 짝수번 곱할 경우
    if B%2 == 0:
        return tmp*tmp % C

    # 홀수번 곱할 경우
    else:
        return tmp*tmp*A % C

print(div(A, B)%C)
