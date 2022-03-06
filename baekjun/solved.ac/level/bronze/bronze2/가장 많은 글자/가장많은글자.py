import sys
from collections import Counter

answer = ''
before_value = False
user_input = sys.stdin.read().replace(' ', '').replace('\n', '')
for key, value in sorted(Counter(user_input).most_common(), key = lambda x : (-x[1], x[0])):
    if before_value and before_value != value:
        break
    answer += key
    before_value = value
print(answer)