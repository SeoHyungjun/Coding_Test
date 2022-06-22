import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

length = len(B)
index = 0
answer = 0
while index <= len(A) - length:
    if A[index:index+length] == B:
        answer += 1
        index += length
    else:
        index += 1

print(answer)