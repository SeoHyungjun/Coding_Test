import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    a_sum, b_sum = 0, 0
    for _ in range(N):
        a, b = sys.stdin.readline().split()
        
        if a == b:
            continue
        elif (a == 'R' and b == 'P') or (a == 'P' and b == 'S') or (a == 'S' and b == 'R'):
            b_sum += 1
        else:
            a_sum += 1

    if a_sum == b_sum:
        print('TIE')
    elif a_sum > b_sum:
        print('Player 1')
    else:
        print('Player 2')