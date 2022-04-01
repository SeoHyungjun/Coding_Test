import sys

def multi_arr(arr):
    answer = 1
    for n in arr:
        answer *= n

    return answer

N = list(map(int, list(sys.stdin.readline().rstrip())))
answer = 'NO'

if len(N) > 1:
    for i in range(1, len(N)):
        left = multi_arr(N[:i])
        right = multi_arr(N[i:])

        if left == right:
            answer = 'YES'
            break

print(answer)