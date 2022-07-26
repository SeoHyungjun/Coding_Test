import sys

N = int(sys.stdin.readline())
temp = [[] for _ in range(101)]
dic = [{} for _ in range(101)]
answer = 0

for i in range(N):
    num = 0
    word = sys.stdin.readline().rstrip()

    for j in word:
        if j not in dic[i]:
            dic[i][j] = str(num)
            num += 1

        temp[i] += dic[i][j]

for i in range(N):
    for j in range(i + 1, N):
        if temp[i] == temp[j]:
            answer += 1

print(answer)