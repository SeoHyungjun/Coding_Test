def str_to_sec(_time):  # 문자열 형식 시간 -> 초
    _time = list(map(int,_time.split(':')))
    return int(_time[0] * 3600 + _time[1] * 60 + _time[2])

def sec_to_str(_sec): # 초 -> 문자열 형식 시간
    return ("%.2d:%.2d:%.2d"%(_sec//3600,(_sec%3600)//60,_sec%60)).lstrip()

def solution(play_time, adv_time, logs):
    play_time_sec = str_to_sec(play_time)
    adv_time_sec = str_to_sec(adv_time)
    if play_time_sec == adv_time_sec:
        return "00:00:00"
    else:
        logs = sorted([log_.split('-') for log_ in logs])
        logs_start_time = [str_to_sec(log_[0]) for log_ in logs]
        logs_end_time = [str_to_sec(log_[1]) for log_ in logs]

        total_time = [0]*360000 # 각 초마다 본 사람 수
        for i in range(len(logs)):
            total_time[logs_start_time[i]] = total_time[logs_start_time[i]] + 1
            total_time[logs_end_time[i]] = total_time[logs_end_time[i]] -1

        # 전체 시간 내에 누적 시청자 수
        for idx in range(1,len(total_time)):
            total_time[idx] += total_time[idx-1]
        
        # 가장 많은 시청자수를 가진 구간 찾기
        sum_time = sum(total_time[:adv_time_sec])
        max_time = sum_time if sum_time > 0 else 0
        max_idx = 0
        for t_time in range(adv_time_sec, play_time_sec+1):
            sum_time += total_time[t_time]
            sum_time -= total_time[t_time-adv_time_sec]
            if sum_time > max_time:
                max_time = sum_time
                max_idx = t_time-adv_time_sec+1

    return sec_to_str(max_idx)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]), "01:30:59")
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")