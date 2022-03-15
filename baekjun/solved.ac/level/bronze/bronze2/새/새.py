import sys

N = int(sys.stdin.readline())

sing_num = 1
answer = 0
while N:
    if sing_num > N:
        sing_num = 1
        continue

    N -= sing_num
    sing_num += 1
    answer += 1

print(answer)