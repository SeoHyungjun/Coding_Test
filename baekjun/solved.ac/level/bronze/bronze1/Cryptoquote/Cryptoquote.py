import sys

T = int(sys.stdin.readline())
for _ in range(T):
    message = sys.stdin.readline().rstrip()
    key = sys.stdin.readline().rstrip()

    key_dic = {}
    for i in range(26):
        key_dic[chr(ord('A') + i)] = key[i]

    answer = ''
    for i, s in enumerate(message):
        if s not in key_dic:
            answer += message[i]
        else:
            answer += key_dic[message[i]]

    print(answer)