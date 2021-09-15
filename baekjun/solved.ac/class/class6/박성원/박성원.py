import sys
import math

def dfs(L, visit, rest):
    if visit == (1<<N) - 1: # 조합의 숫자가 4개라면 1111일 경우 == 모두 연결 되었을 때
        if rest == 0:
            return 1 # 나머지가 0이면 1
        return 0 # 나머지가 0이 아니면 0

    if dp[visit][rest] == -1: # 방문 안된 경우이므로 계산, 이미 계산된 경우 바로 값 return
        dp[visit][rest] = 0 # 방문 처리
        for i in range(N):
            if visit & (1<<i) == 0: # 확인 안한 숫자인 경우
                dp[visit][rest] += dfs(L + arr_len[i], visit | (1<<i), (rest + squared[i][L]) % K)

    return dp[visit][rest]

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
K = int(sys.stdin.readline())

dp = [[-1]*K for _ in range(1<<N)] # dp[1][2] =>  [0001][2] 즉, 4개의 숫자 중 1개(4번째 위치가 1이므로)를 선택했을 때 나머지가 2가 나오는 경우의 수
arr_len = [len(str(i)) for i in arr]

# 집합의 숫자들이 위치가 10**n 자리가 될 수 있으므로 미리 계산
squared = [[-1]*sum(arr_len) for _ in range(N)]
for i in range(N):
    for j in range(sum(arr_len)):
        squared[i][j] = arr[i] * (10**j) % K

dfs(0, 0, 0) 
if dp[0][0] == 0:
    print('0/1')
else:
    factorial_N = math.factorial(N)
    gcd_factorial_N_to_answer = math.gcd(factorial_N, dp[0][0])
    print(dp[0][0]//gcd_factorial_N_to_answer, '/',factorial_N//gcd_factorial_N_to_answer, sep = '')