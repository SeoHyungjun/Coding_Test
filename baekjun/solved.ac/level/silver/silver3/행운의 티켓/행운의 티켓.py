import sys

def is_same(arr):
    return True if sum(arr[:len(arr)//2]) == sum(arr[len(arr)//2:]) else False

def solution(arr):
    end = len(arr) - 1 if len(arr) & 1 else len(arr)

    while end > 0:
        i, answer = 0, 0

        while i + end <= len(arr):
            if is_same(arr[i:i+end]):
                answer = end
                return answer
            i += 1
        end -= 2
    return 0

arr = list(map(int, sys.stdin.readline().rstrip()))
print(solution(arr))