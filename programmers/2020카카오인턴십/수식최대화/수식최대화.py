#2021-02-24 17:30 -> 

from itertools import permutations
import re

def solution(expression):
    answer = 0
    
    # exp안에 expression에서 발견된 연산자를 추가
    exp = [e for e in ['*', '+', '-']if e in expression]
    print(exp)
    '''
    if '*' in expression:
        exp.append('*')
    if '+' in expression:
        exp.append('+')
    if '-' in expression:
        exp.append('-')
    '''
    
    # exp안에 연산자가 들어있고, 그 갯수를 알 수 있으므로 순열을 통해 경우의수 모두 출력
    per = list(permutations(exp, len(exp)))

    # 정규 포현식을 사용해 숫자, 연산자를 나누기
    fi_exp = re.split(r'(\D)', expression)
    print(fi_exp)
    '''
    com = re.compile('(\d+[*+-]?)')
    re_exp = com.findall(expression)
    
    fi_exp = []
    for a in re_exp:
        if '*' in a or '+' in a or '-' in a:
            fi_exp.append(a[:-1])
            fi_exp.append(a[-1])
        else:
            fi_exp.append(a)
    '''

    # 순열 순서대로 하나씩 연산처리
    for p in per:
        text = fi_exp[:]
        for e in p:
            while e in text:
                index = text.index(e)
                if e == '*':
                    text[index-1] = str(int(text[index-1]) * int(text[index+1]))
                if e == '+':
                    text[index-1] = str(int(text[index-1]) + int(text[index+1]))
                if e == '-':
                    text[index-1] = str(int(text[index-1]) - int(text[index+1]))
                
                del text[index]
                del text[index]
    
        
        answer = max(answer, abs(int(text[0])))
    
    return answer


expression = "100-200*300-500+20"
print(solution(expression))