import sys

N, M = map(int, sys.stdin.readline().split())

trust = list(map(int, sys.stdin.readline().split()))

partys = []
for _ in range(M):
    partys.append(list(map(int, sys.stdin.readline().split()))[1:])

if trust[0] == 0:
    answer = M
else:
    trust = trust[1:]
    recheck = True
    while recheck:
        recheck = False
        for party in partys:
            diff_party = set(party).difference(trust)
            if not ( len(diff_party) == 0 or len(diff_party) == len(party) ):
                trust = list(set(trust+party))
                recheck = True
    
    answer = 0
    for party in partys:
        diff_party = set(party).difference(trust)
        if len(diff_party) == len(party):
            answer += 1

print(answer)
