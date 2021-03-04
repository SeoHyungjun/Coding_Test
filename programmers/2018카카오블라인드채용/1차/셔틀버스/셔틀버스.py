#2021-03-03 14:11 -> 14:52

def solution(n, t, m, timetable):
    answer = 0
    #mintable = []
    # n 셔틀운행횟수, t 운행간격, m 최대탑승인원

    # timetable안의 시:분 을 분으로 통일
    # for time in timetable:
    #     hh, mm = map(int, time.split(':'))
    #     mintable.append(hh*60 + mm)
    mintable = sorted([int(time[:2])*60 + int(time[3:]) for time in timetable])
    #mintable.sort()

    for time in range(540, 540 + (n-1)*t + 1, t):
        in_person = 0
        for _ in range(m):
            if mintable and mintable[0] <= time:
                in_person += 1
                answer = mintable[0]
                del mintable[0]

        if time == 540 + (n-1)*t:
            print('in_person, m = ', in_person, m)
            if in_person == m:
                answer -= 1
            elif in_person < m:
                answer = 540 + (n-1) * t

    return '%02d:%02d' %(answer//60, answer%60)

timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(1, 1, 5, timetable))
timetable = ["09:10", "09:09", "08:00"]
print(solution(2, 10, 2, timetable))
timetable = ["09:00", "09:00", "09:00", "09:00"]
print(solution(2, 1, 2, timetable))
timetable = ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(10, 60, 10, timetable))