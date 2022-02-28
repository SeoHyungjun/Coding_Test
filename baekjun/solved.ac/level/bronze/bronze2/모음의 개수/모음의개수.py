import sys

vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

while True:
    user_input = sys.stdin.readline().rstrip()
    if user_input == '#':
        break

    answer = 0
    for alp in user_input:
        if alp in vowel_set:
            answer += 1

    print(answer)