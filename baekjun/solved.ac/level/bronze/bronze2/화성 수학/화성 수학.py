import sys

N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(input().split())
    answer = float(arr.pop(0))
    for i in arr:
        if i == '@':
            answer *= 3
        elif i == '%':
            answer += 5
        elif i == '#':
            answer -= 7
    
    print("%0.2f" % answer)