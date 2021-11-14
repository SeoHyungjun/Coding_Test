import sys
input = sys.stdin.readline

a = 0
b = 0
c = 0

def check_all_same(paper):
    if len(paper) == 1:
        return paper[0][0]
    
    zero = 0
    one = 0
    m_one = 0

    for i in paper:
        if zero == 0 and 0 in i:
            zero = 1
        if one == 0 and 1 in i:
            one = 1
        if m_one == 0 and -1 in i:
            m_one = 1
        
        if zero + one + m_one > 1:
            return 4
    if zero == 1:
        return 0
    elif one == 1:
        return 1
    elif m_one == 1:
        return -1

def count_number(paper):
    global a, b, c
    state = check_all_same(paper)
    size = len(paper)//3
    if state == 4:
        for i in range(3):
            for j in range(3):
                count_number([arr[j*size:(j+1)*size] for arr in paper[i*size:(i+1)*size]])
    elif state == -1:
        a += 1
    elif state == 0:
        b += 1
    elif state == 1:
        c += 1


n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

count_number(paper)

print(a,b,c)