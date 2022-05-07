import sys
from datetime import datetime

def change_day(st):
    answer = 0

    for year in range(st, st+1000):
        if year % 400 == 0:
            answer += 366
        elif year % 100 == 0:
            answer += 365
        elif year % 4 == 0:
            answer += 366
        else:
            answer += 365

    return answer

def d_day(today, dday):
    year = change_day(today[0])

    today = datetime(year=today[0], month=today[1], day=today[2])
    dday = datetime(year=dday[0], month=dday[1], day=dday[2])

    day = (dday - today).days

    if day >= year:
        return 'gg'
    else:
        return f'D-{day}'


today = list(map(int, sys.stdin.readline().split()))
dday = list(map(int, sys.stdin.readline().split()))
print(d_day(today, dday))