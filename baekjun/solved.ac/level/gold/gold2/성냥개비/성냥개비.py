import sys

def find_max(num):
    answer = ''
    if num % 2 != 0:
        answer += '7'
        num -= 3

    while num:
        answer += '1'
        num -= 2
    return answer

dic = {2:1, 3:7, 4:4, 5:2, 6:0, 7:8}

N = int(sys.stdin.readline())
dp = [0, 0, 1, 7, 4, 2, 6, 8, 10]

for i in range(9, 101):
    tmp = []
    for j in range(2, 8):
        tmp.append(dp[i-j]*10 + dic[j])
    
    dp.append(min(tmp))

for _ in range(N):
    num = int(sys.stdin.readline())

    print(dp[num], find_max(num))