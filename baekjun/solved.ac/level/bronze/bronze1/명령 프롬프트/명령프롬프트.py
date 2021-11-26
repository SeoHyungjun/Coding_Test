import sys

N = int(sys.stdin.readline())
file_list = [sys.stdin.readline().rstrip() for _ in range(N)]

answer = list(file_list[0])
for i in range(1, N):
    for j in range(len(answer)):
        if answer[j] == '?' or answer[j] == file_list[i][j]:
            continue

        answer[j] = '?'

print(''.join(answer))