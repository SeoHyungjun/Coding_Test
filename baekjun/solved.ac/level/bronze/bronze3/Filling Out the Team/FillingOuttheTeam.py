import sys

while True:
    a, b, c = map(float, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0:
        break

    check = False
    answer = []
    if a <= 4.5 and b >= 150 and c >= 200:
        answer.append('Wide Receiver')
        check = True
    if a <= 6.0 and b >= 300 and c >= 500:
        answer.append('Lineman')
        check = True
    if a <= 5.0 and b >= 200 and c >= 300:
        answer.append('Quarterback')
        check = True

    print('No positions') if not answer else print(*answer)