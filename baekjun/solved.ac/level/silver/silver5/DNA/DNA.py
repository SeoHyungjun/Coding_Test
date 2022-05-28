import sys

nucleotide = {'A':0, 'C':1, 'G':2, 'T':3, 0:'A', 1:'C', 2:'G', 3:'T'}

N, M = map(int, sys.stdin.readline().split())
dnas = [sys.stdin.readline().rstrip() for _ in range(N)]

answer = ''
answer_cnt = 0
for i in range(M):
    cnt = [0]*4
    for j in range(N):
        cnt[nucleotide[dnas[j][i]]] += 1

    max_cnt = max(cnt)
    for j in range(4):
        if max_cnt == cnt[j]:
            answer += nucleotide[j]
            answer_cnt += N-cnt[j]
            break

print(answer)
print(answer_cnt)