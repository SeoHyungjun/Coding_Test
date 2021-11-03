import sys

K, N, M = map(int, sys.stdin.readline().split())
print(K*N - M if M <= K*N else 0)