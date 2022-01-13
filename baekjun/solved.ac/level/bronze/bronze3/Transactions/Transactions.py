import sys

while True:
    a, com, b = sys.stdin.readline().split()

    if a == '0' and com == 'W' and b == '0':
        break

    if com == 'W':
        b = '-' + b
    answer = int(a)+int(b)

    if answer >= -200:
        print(answer)
    else:
        print('Not allowed')