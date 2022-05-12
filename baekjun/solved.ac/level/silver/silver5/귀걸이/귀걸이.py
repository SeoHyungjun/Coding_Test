import sys

cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    students = [sys.stdin.readline().rstrip() for _ in range(N)]
    confiscated = set()
    for _ in range(2*N-1):
        num, _ = sys.stdin.readline().split()
        if num in confiscated:
            confiscated.remove(num)
        else:
            confiscated.add(num)

    answer = confiscated.pop()
    print(cnt, students[int(answer) - 1])
    cnt += 1