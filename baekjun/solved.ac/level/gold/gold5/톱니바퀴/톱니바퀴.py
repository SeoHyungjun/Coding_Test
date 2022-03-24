import sys

def sum_tooth():
    tmp = 1
    answer = 0
    for t in saw_tooth:
        if t[0] == '1':
            answer += tmp
        tmp *= 2

    return answer

def change_tooth(num, direction):
    if direction == 1:
        saw_tooth[num] = saw_tooth[num][-1] + saw_tooth[num][:-1]
    else:
        saw_tooth[num] = saw_tooth[num][1:] + saw_tooth[num][0]

def rotation_tooth(num, direction, before_left, before_right):
    for i in range(num+1, 4):
        if before_right == saw_tooth[i][6]:
            break

        new_direction = direction if num % 2 == i % 2 else -1 * direction
        before_right = saw_tooth[i][2]
        change_tooth(i, new_direction)

    for i in range(num-1, -1, -1):
        if before_left == saw_tooth[i][2]:
            break

        new_direction = direction if num % 2 == i % 2 else -1 * direction
        before_left = saw_tooth[i][6]
        change_tooth(i, new_direction)

saw_tooth = [sys.stdin.readline().rstrip() for _ in range(4)]
K = int(sys.stdin.readline())
for _ in range(K):
    num, direction = map(int, sys.stdin.readline().split())
    before_left, before_right = saw_tooth[num-1][6], saw_tooth[num-1][2]
    change_tooth(num-1, direction)
    rotation_tooth(num-1, direction, before_left, before_right)

print(sum_tooth())