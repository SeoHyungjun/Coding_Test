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
    #print(play_time, adv_time)

    start_time = []

    for i in range(len(logs)):
        logs[i] = logs[i].split("-")
        for j in range(len(logs[i])):
            logs[i][j] = logs[i][j].split(':')
            logs[i][j] = change_time(logs[i][j])
            if j == 0:
                start_time.append((logs[i][j], logs[i][j]+adv_time))
    logs = sorted(logs, key = lambda x : x[0])
    print('logs =', logs)

    for st, en in start_time:
        if play_time >= en:
            time_check = 0
            for log_st, log_en in logs:
                if log_st > en:
                    break
                if not (log_st > en or log_en < st):
                    time_check += min(en, log_en) - max(st, log_st)
            if time_check != 0:
                answer.append((st, time_check))

    answer = sorted(answer, key=lambda x : (-1*x[1], x[0]))
    return rechange_time(answer[0][0])

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))