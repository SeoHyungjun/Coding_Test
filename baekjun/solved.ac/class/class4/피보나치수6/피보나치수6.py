import sys

N = int(sys.stdin.readline())

matrix = [[1, 1], [1, 0]]

def mul(A, B):
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += (A[i][k] * B[k][j] % 1000000007)
            ans[i][j] %= 1000000007
    return ans

def bin_matrix(n):
    if n == 1:
        return matrix

    tmp = bin_matrix(n//2)
    if n%2 == 0:
        return mul(tmp, tmp)

    else:
        return mul(matrix, mul(tmp, tmp))
    
print(bin_matrix(N)[0][1])