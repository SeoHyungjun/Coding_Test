from collections import defaultdict

while True:
    try:
        a = input()
        b = input()

        a_dic = defaultdict(int)
        answer = []

        for alpha in a:
            a_dic[alpha] += 1

        for alpha in b:
            if a_dic[alpha] == 0:
                continue
            a_dic[alpha] -= 1
            answer.append(alpha)

        print(''.join(sorted(answer)))

    except:
        break