import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    print('1', op)
    #op = [list(y) for y in permutations(op)]
    op = list(permutations(op, len(op)))
    print('2', op)
    #ex = re.split(r'(\D)',expression)
    ex = re.split('(\D)',expression)
    print(ex)

    '''
    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)
    '''


expression = "100-200*300-500+20"
print(solution(expression))