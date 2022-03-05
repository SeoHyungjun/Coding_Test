import sys

AB = sys.stdin.readline().rstrip()

if len(AB) == 2:
    print(int(AB[0]) + int(AB[1]))
elif len(AB) == 4:
    print(20)
elif AB[1] == '0':
    print(10 + int(AB[2]))
else:
    print(int(AB[0]) + 10)