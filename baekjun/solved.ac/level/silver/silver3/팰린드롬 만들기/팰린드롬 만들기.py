import sys
from collections import defaultdict

name = sys.stdin.readline().rstrip()
alpha = defaultdict(int)
for a in name:
    alpha[a] += 1

odd_cnt = 0
odd = ''
alpha_left = ''
for key in sorted(alpha.keys()):
    if alpha[key] % 2 == 1:
        odd_cnt += 1
        odd += key
    alpha_left += key * (alpha[key] // 2)

if odd_cnt <= 1:
    print(alpha_left + odd + alpha_left[::-1])
else:
    print("I'm Sorry Hansoo")