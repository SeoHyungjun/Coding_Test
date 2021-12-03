import sys

input_string = sys.stdin.readline().rstrip()

answer = input_string[0]

for i in range(1, len(input_string)):
    if answer[-1] < input_string[i]:
        answer = input_string[i] + answer
    else:
        answer = answer + input_string[i]

print(answer[::-1])