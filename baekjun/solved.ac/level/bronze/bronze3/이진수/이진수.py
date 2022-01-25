import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = bin(int(sys.stdin.readline())).replace('0b', '')[::-1]

    answer = []
    for i in range(len(N)):
        if N[i] == '1':
            answer.append(i)
    print(*answer)