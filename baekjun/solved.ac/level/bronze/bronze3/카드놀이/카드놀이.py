import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
point = [0, 0]
winner = []

for i in range(10):
    if A[i] > B[i]:
        point[0] += 3
        winner.append('A')
    elif A[i] < B[i]:
        point[1] += 3
        winner.append('B')
    else:
        point[0] += 1
        point[1] += 1
        winner.append('D')

print(*point)
if point[0] > point[1]:
    print('A')
elif point[0] < point[1]:
    print('B')
else:
    while winner:
        tmp = winner.pop()

        if tmp != 'D':
            break

    print(tmp)