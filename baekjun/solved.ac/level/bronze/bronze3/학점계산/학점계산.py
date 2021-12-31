import sys

dic = {'A':4, 'B':3, 'C':2, 'D':1, '+':0.3, '0':0.0, '-':-0.3, 'F':0.0}

answer = 0
for i in sys.stdin.readline().rstrip():
    answer += dic[i]
print(answer)