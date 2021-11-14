import sys

def KMP(string, pattern):
    cnt = 0
    pos = []

    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = fail_function[j-1]

        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                cnt += 1
                pos.append(i - len(pattern) + 2)
                j = fail_function[j]

            else:
                j += 1

    return cnt, pos


def make_fail_function():
    table = [0] * len(P)

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = table[j-1]

        if P[i] == P[j]:
            j += 1
            table[i] = j

    return table

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

# 실패 함수 만들기
# 주어진 패턴에서 특정 위치에서 실패(일치 하지 않음)했을 경우 어디부터 시작해야할 지 알려주는 테이블?
fail_function = make_fail_function()
cnt, pos = KMP(T, P)

print(cnt)
print(*pos)