import sys
import re

T = int(sys.stdin.readline())
for _ in range(T):
    print('YES' if re.fullmatch('(100+1+|01)+', sys.stdin.readline().rstrip()) else 'NO')