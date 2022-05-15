import sys

user_input = sys.stdin.readline().rstrip()

if '0' not in user_input:
    print('0')
    exit()

zero_cnt, one_cnt = 0, 0
before = None
for c in user_input:
    if before == c:
        continue

    if c == '0':
        zero_cnt += 1
        before = '0'
    else:
        one_cnt += 1
        before = '1'

print(min(zero_cnt, one_cnt))