import sys

gear1 = sys.stdin.readline().rstrip()
gear2 = sys.stdin.readline().rstrip()

# 둘이 서로 맞물리는 경우가 없을경우 -> 최악의 경우
answer = len(gear1) + len(gear2)

if len(gear1) > len(gear2):
    gear1, gear2 = gear2, gear1

# 위의 기어가 왼쪽에서 오른쪽으로 가면서 체크
for i in range(1, len(gear1)): # i개를 비교
    avail = True
    for j in range(i):
        if gear1[len(gear1) - i + j] == '2' and gear2[j] == '2':
            avail = False
            break

    if avail:
        answer = min(answer, len(gear1) + len(gear2) - i)

# 위의 기어가 오른쪽에서 왼쪽으로 가면서 체크
for i in range(1, len(gear1)):
    avail = True
    for j in range(i):
        if gear1[j] == '2' and gear2[len(gear2) - i + j] == '2':
            avail = False
            break

    if avail:
        answer = min(answer, len(gear1) + len(gear2) - i)

# 긴 기어 안에서 짧은 기어를 체크
for i in range(len(gear2) - len(gear1) + 1):
    avail = True
    for j in range(len(gear1)):
        if gear1[j] == '2' and gear2[i + j] == '2':
            avail = False
            break
    
    if avail:
        answer = len(gear2)
        break

print(answer)
