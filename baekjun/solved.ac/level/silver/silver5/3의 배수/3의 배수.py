import sys

def decrease(num):
    new_num = 0
    for i in num:
        new_num += int(i)

    return str(new_num)

X = sys.stdin.readline().rstrip()
cnt = 0
while len(X) != 1:
    X = decrease(X)
    cnt += 1

print(cnt)
print('YES' if int(X) % 3 == 0 else 'NO')