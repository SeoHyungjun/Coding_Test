import sys

N = int(sys.stdin.readline())
div_num = N // 2 + 1
if N % 2 == 0:
    row = col = div_num
else:
    row = div_num + 1
    col = div_num 

print(row * col)