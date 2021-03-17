# 2021-03-11 18:37 -> 18:39

def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]


s = "abcde"
print(solution('abcde'))
print(solution('qwer'))