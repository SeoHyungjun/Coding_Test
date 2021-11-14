import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def solve():
    answer = 0

    for i in airplane:
        i = find(i)
        if i == 0:
            break
        parent[i] = parent[i-1]
        answer += 1

    return answer

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
airplane = [int(sys.stdin.readline()) for _ in range(P)]
parent = [0] + [i+1 for i in range(G)]

print(solve())