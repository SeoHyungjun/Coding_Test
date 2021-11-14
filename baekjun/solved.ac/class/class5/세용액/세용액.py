import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

def solve():
    answer = []
    tmp = float('inf')
    for i in range(len(arr)-2):
        start, end = i+1, len(arr)-1

        while start < end:
            sum = arr[i] + arr[start] + arr[end]
            abssum = abs(sum)

            if abssum < tmp:
                tmp = abssum
                answer = [arr[i], arr[start], arr[end]]

            if sum > 0:
                end -= 1
            elif sum < 0:
                start += 1
            else:
                return answer
                
    return answer

print(*solve())