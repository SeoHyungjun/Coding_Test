import sys

while True:
    cur = sys.stdin.readline().rstrip()
    if cur == '*': break

    flag = True
    for i in range(1, len(cur) - 1):
        check = set()
        for j in range(len(cur) - i):
            if cur[j] + cur[j + i] in check:
                flag = False
                break
            check.add(cur[j] + cur[j + i])
        if not flag: break

    print(cur, end = " is ")
    print("surprising." if flag else "NOT surprising.")