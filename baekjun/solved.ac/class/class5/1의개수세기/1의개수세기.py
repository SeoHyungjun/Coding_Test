import sys

def cal(x):
    x = str(bin(x))[2:]
    len_x = len(x) - 1
    start = 2**(len_x-1)
    answer = 0
    count_one = 0

    for i in range(len_x+1):
        if x[i] == '1':
            answer += int((len_x - i) * start + 2**(len_x-i) * count_one + 1)
            count_one += 1
        start //= 2
    
    return answer

A, B = map(int, sys.stdin.readline().split())

print(cal(B)-cal(A-1))
#print(cal(B) - cal(A-1))
'''
1100

0000
0001
0010
0011
0100
0101
0110
0111

1000
1001
1010
1011

1100
'''