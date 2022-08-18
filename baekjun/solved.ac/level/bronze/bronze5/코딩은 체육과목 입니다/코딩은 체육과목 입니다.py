import sys
import math

N = int(sys.stdin.readline())
answer = ''
for _ in range(math.ceil(N/4)):
    answer += 'long '
print(answer + 'int')