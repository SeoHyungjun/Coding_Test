# 2021-02-10 13:50 -> 14:24

# 문자열의 길이가 1일때 예외처리 안했더니 문제 생김...
# splited에 1 ~ 전에 문자열의 반, 단위로 나누어 저장
# 그 후에 count를 통해 같은 문자의 수를 세고, 뒤에 문자와 다를 경우 저장

def solution(s):
    answer = []
    len_string = len(s)

    if len_string == 1:
        return 1

    for i in range(1, (len_string // 2) + 1):
        splited = [s[j:j+i] for j in range(0, len(s), i)]

        count = 1
        arr = []
        for j in range(len(splited)):
            if j != len(splited)-1 and splited[j] == splited[j+1]:
                count += 1
            else:
                if count == 1: arr.append(splited[j])
                else: arr.append(str(count) + splited[j])
                count = 1

        answer.append(len("".join(arr)))

    return min(answer)


s = "aabbaccc"
print(solution(s))