# 2021-02-09 21:11 -> 22:02


def check_str(string):
    left = 0
    right = 0
    index = -1
    balance = True

    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1

        if right == left and index == -1:
            index = i
        
        if right > left:
            balance = False

    return index, balance


def solution(p):
    answer = ''

    if p == '':
        return ''

    uv_index, check_balance = check_str(p)
    
    if check_balance == True:
        return p
    else:
        u = p[:uv_index+1]
        v = p[uv_index+1:]

        uv_index, check_balance = check_str(u)
        if check_balance == True:
            return u + solution(v)
        else:
            start = '('
            start = start + solution(v) + ')'
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    start += ')'
                else:
                    start += '('
            return start


p = "(()())()"
#p = "()))((()"
#p = ")("
print(solution(p))