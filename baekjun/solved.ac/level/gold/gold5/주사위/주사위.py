import sys

diff = {0:5, 5:0, 1:4, 4:1, 2:3, 3:2}
near3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (5, 1, 2), (5, 1, 3), (5, 2, 4), (5, 3, 4)]

def min3():
    answer = float('inf')
    for a, b, c in near3:
        answer = min(answer, arr[a] + arr[b] + arr[c])

    return answer

def min2():
    answer = float('inf')
    for i in range(6):
        for j in range(6):
            if i != j and diff[i] != j:
                answer = min(answer, arr[i] + arr[j])
    return answer

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(sum(arr) - max(arr))
else:
    m3 = min3()
    m2 = min2()
    m1 = min(arr)
    num2 = (N - 1) * 4 + (N - 2) * 4
    num1 = (N - 1) * (N - 2) * 4 + (N - 2) * (N - 2) 
    print(4*m3 + num2 * m2 + num1 * m1)