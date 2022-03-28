import sys

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

S.append(0)
S.sort()

for i in range(len(S)-1):
    if S[i] == N or S[i+1] == N:
        answer = 0
        break

    elif S[i] < N < S[i+1]:
        answer = (N - S[i])*(S[i+1] - N) - 1
        break
        
print(answer)