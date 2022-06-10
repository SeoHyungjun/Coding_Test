import sys

A, B = sys.stdin.readline().split()

answer = 50
for i in range(len(B) - len(A) + 1):
    same_cnt = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            same_cnt += 1

    answer = min(answer, same_cnt)

print(answer)