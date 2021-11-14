import sys

M = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if M < 2:
    print('Before')
elif M > 2:
    print('After')
else:
    if D < 18:
        print('Before')
    elif D > 18:
        print('After')
    else:
        print('Special')