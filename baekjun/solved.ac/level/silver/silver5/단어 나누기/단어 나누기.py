import sys

user_input = sys.stdin.readline().rstrip()

answer = []
for i in range(len(user_input)-2):
    for j in range(i+1, len(user_input)-1):
        for k in range(j+1, len(user_input)):
            t = user_input[:j][::-1] + user_input[j:k][::-1] + user_input[k:][::-1]
            answer.append(t)
print(min(answer))