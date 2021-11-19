import sys

arr = [('', 0)]
for _ in range(int(sys.stdin.readline())):
    com, a, b = sys.stdin.readline().rstrip().split()

    if com == 'type':
        arr.append((arr[-1][0] + a, int(b)))

    else:
        index = len(arr) - 1
        while index > 0 and arr[index][1] > int(b) - int(a) - 1:
            index -= 1

        arr.append((arr[index][0], int(b)))

print(arr[-1][0])