import re
from collections import Counter

def solution(s):
    answer = []

    s = Counter(re.findall('\d+', s))
    
    return [int(a) for a, b in sorted(s.items(), key = lambda x : x[1], reverse = True)]


s = '{{2},{2,1},{2,1,3},{2,1,3,4}}'
print(solution(s))