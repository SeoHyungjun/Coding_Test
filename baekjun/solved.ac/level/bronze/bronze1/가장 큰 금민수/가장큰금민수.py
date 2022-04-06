import sys

N = int(sys.stdin.readline())
set_answer = set(['4', '7'])

for i in range(N, 3, -1):
    if set(str(i)) <= set_answer:
        print(i)
        break