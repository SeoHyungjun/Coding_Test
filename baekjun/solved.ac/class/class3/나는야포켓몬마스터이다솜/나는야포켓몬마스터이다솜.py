import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_dic = {}
num_dic = {}

for i in range(1, n+1):
    name = input().rstrip('\n')
    name_dic[name] = i
    num_dic[i] = name

for _ in range(m):
    quiz = input().rstrip('\n')
    if quiz.isdigit():
        print(num_dic[int(quiz)])
    else:
        print(name_dic[quiz])