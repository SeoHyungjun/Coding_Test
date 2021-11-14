import sys
import re

n = int(sys.stdin.readline())
arr_len = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip('\n')
pn = 'I' + 'OI' * n

print(list(re.findall('I(OI*)'.format(pn), arr)))