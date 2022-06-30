import sys

char_num = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

def change_num2char(num):
    char_arr = []
    
    while num > 0:
        char_arr.append(char_num[num % 10])
        num //= 10

    return ' '.join(reversed(char_arr))

M, N = map(int, sys.stdin.readline().split())
arr = [i for i in range(M, N+1)]
arr.sort(key=lambda x: change_num2char(x))

for i, n in enumerate(arr):
    if i % 10 == 9:
        print(n)
    else:
        print(n, end = ' ')