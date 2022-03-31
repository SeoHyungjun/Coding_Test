import sys

def get_point(n, tn):
    L = n.count('L') + tn.count('L')
    O = n.count('O') + tn.count('O')
    V = n.count('V') + tn.count('V')
    E = n.count('E') + tn.count('E')
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

answer = []
yeondu = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

for _ in range(N):
    team_name = sys.stdin.readline().rstrip()
    answer.append((get_point(yeondu, team_name), team_name))
answer.sort(key=lambda x : (-x[0], x[1]))

print(answer[0][1])