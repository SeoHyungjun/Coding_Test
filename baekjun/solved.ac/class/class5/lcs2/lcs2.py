import sys

def solve():
    a = ' '+sys.stdin.readline().rstrip()
    b = ' '+sys.stdin.readline().rstrip()

    dp = [[0] * len(a) for _ in range(len(b))]

    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if b[i] == a[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    answer = ''
    tmp = dp[i][j]
    while dp[i][j] > 0:
        if dp[i-1][j] == tmp:
            i -= 1
        elif dp[i][j-1] == tmp:
            j -= 1
        else:
            answer += a[j]
            i -= 1
            j -= 1
            tmp = dp[i][j]

    print(len(answer))
    print(answer[::-1])

solve()