import sys

def combi(n):
    return (n-1) * (n-2) * (n-3) // 6

J = int(sys.stdin.readline())
print(combi(J))