from collections import Counter
import re

def solution(inp_str):
    answer = []

    # 1번 비번 길이 8<= x <= 15
    if not (8 <= len(inp_str) <= 15):
        answer.append(1)

    ch= [re.compile('[A-Z]'), re.compile('[a-z]'), re.compile('[0-9]'), re.compile(r'[~!@#$%^&*]')]


    # 2번 ch_1~4를 제외한 문자 포함되면 안됨
    if re.findall('[^A-Za-z0-9~!@#$%^&*]', inp_str):
        answer.append(2)


    # 3번 ch_1~4 중 몇개를 포함하는지?
    count = 0
    for c in ch:
        if re.findall(c, inp_str):
            count += 1
    if count < 3:
        answer.append(3)


    # 4번 같은 문자가 4개이상 연속될경우
    matches = re.findall(r'((.)\2{3})', inp_str)
    if matches:
        #print('m==', matches)
        answer.append(4)


    # 5번 한 문자가 5개이상 포함 x
    check5 = Counter(inp_str)
    for s in check5:
        if check5[s] >= 5:
            answer.append(5)
            break


    # 만약 암것도 없다면 0 추가
    if not answer:
        answer.append(0)

    return answer


print(solution("AaTa+!12-3"))
print(solution("aaaaZZZZ)"))
print(solution("CaCbCgCdC888834A"))
print(solution("UUUUU"))
print(solution("ZzZz9Z824"))
print(solution('----'))
