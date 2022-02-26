import sys
from collections import defaultdict

sum_dic = defaultdict(int)
S1, S2, S3 = map(int, sys.stdin.readline().split())

for i in range(S1):
    for j in range(S2):
        for k in range(S3):
            sum_dic[i+j+k+3] += 1

print(sorted(sum_dic.items(), key = lambda x: (-x[1], x[0]))[0][0])