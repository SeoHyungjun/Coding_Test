import sys

def num2value(num):
    return (ord(num[0])-ord('A'))*(26**2) + (ord(num[1])-ord('A'))*26 + ord(num[2]) - ord('A')

N = int(sys.stdin.readline())
for _ in range(N):
    part_number = sys.stdin.readline().split('-')

    if abs(num2value(part_number[0]) - int(part_number[1])) <= 100:
        print('nice')
    else:
        print('not nice')