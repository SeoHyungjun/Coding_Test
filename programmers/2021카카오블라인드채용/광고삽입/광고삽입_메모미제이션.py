def change_time(ti):
    return 3600*int(ti[0]) + 60*int(ti[1]) + int(ti[2])

def rechange_time(ti):
    return '%02d:%02d:%02d' % (int(ti//3600),int(ti%3600//60),int(ti%3600%60))

def solution(play_time, adv_time, logs):
    play_time, adv_time = change_time(play_time.split(':')), change_time(adv_time.split(':'))
    time_map = [0] * (play_time+1)

    for log in logs:
        start, end = log.split('-')
        time_map[change_time(start.split(':'))] += 1
        time_map[change_time(end.split(':'))] -= 1

    for i in range(1, play_time+1):
        time_map[i] += time_map[i-1]

    for i in range(1, play_time+1):
        time_map[i] += time_map[i-1]

    min_time = 0
    max_see = time_map[adv_time-1]
    for i in range(adv_time, play_time+1):
        cur_see = time_map[i] - time_map[i-adv_time]
        if cur_see > max_see:
            max_see = cur_see
            min_time = i-adv_time+1


    return (rechange_time(min_time))
    


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))