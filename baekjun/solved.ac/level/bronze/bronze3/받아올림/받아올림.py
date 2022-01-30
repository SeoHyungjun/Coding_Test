import sys

while True:
    a, b = sys.stdin.readline().split()

    if a == '0' and b == '0':
        break

    a = list(a[::-1])
    b = list(b[::-1])
    if len(a) > len(b):
        a, b = b, a
    for i in range(len(b) - len(a)):
        a.append('0')

    answer = 0
    carry = 0
    for i in range(len(b)):
        sum_ab = int(a[i]) + int(b[i]) + carry
        carry = sum_ab//10

        answer += carry

    print(answer)