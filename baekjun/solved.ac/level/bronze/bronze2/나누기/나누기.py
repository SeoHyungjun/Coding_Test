import sys

N = sys.stdin.readline().rstrip()
F = int(sys.stdin.readline())
if len(N) <= 2:
    prev = ''
else:
    prev = N[:-2]

stop_flag = False
for i in range(10):
    for j in range(10):
        if int(prev + str(i) + str(j)) % F == 0:
            answer = str(i) + str(j)
            stop_flag = True
            break
    if stop_flag:
        break

print(answer)