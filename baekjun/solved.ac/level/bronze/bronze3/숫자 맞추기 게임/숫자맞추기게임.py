import sys

T = 0
while True:
    T += 1
    N0 = int(sys.stdin.readline())
    if N0 == 0:
        break

    N1 = 3*N0
    N2 = N1/2 if N1 % 2 == 0 else (N1+1)/2
    N3 = 3*N2
    N4 = N3//9

    answer = 'even' if N1%2 == 0 else 'odd'
    print('%d. %s %d'%(T, answer, N4))