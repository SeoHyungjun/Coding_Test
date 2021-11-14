def change_time(ti):
    return 3600*int(ti[0]) + 60*int(ti[1]) + int(ti[2])

def rechange_time(ti):
    h = int(ti // 3600)
    ti %= 3600
    m = int(ti // 60)
    ti %= 60
    s = int(ti)
    return '%02d:%02d:%02d' % (h,m,s)

def solution(play_time, adv_time, logs):
    answer = []

    if play_time == adv_time:
        return '00:00:00'

    play_time, adv_time = change_time(play_time.split(':')), change_time(adv_time.split(':'))

    for i in range(len(logs)):
        logs[i] = logs[i].split("-")
        for j in range(len(logs[i])):
            logs[i][j] = logs[i][j].split(':')
            logs[i][j] = change_time(logs[i][j])

    print(logs)
    time_map = [0] * play_time
    for st, en in logs:
        for i in range(st, en):
            time_map[i] += 1

    max_sum = 0
    min_time = 360000
    for i in range(play_time-adv_time):
        if max_sum < sum(time_map[i:adv_time]):
            min_time = i

    print(rechange_time(i))