import sys

octopus = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    input_num = sys.stdin.readline().rstrip()

    if input_num == '#':
        break

    changed_num = 0
    multi_flag = 1

    for i in range(len(input_num)-1, -1, -1):
        changed_num += multi_flag * octopus[input_num[i]]
        multi_flag *= 8

    print(changed_num)