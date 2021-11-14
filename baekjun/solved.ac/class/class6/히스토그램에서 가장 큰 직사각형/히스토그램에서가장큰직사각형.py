import sys


def find_biggest_area():
    answer = 0
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            tmp = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            #print('\t%d * % d= %d'%(width, tmp, width * tmp))
            answer = max(answer, width * tmp)

        stack.append(i)

    while stack:
        tmp = arr[stack.pop()]
        width = len(arr) if not stack else len(arr) - stack[-1] - 1
        answer = max(answer, width * tmp)

    return answer


while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break

    arr = arr[1:]
    print(find_biggest_area())