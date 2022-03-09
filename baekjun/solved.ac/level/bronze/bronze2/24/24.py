import sys

def change_time2sec(t):
    return t[0]*3600 + t[1]*60 + t[2]

def change_sec2time(s):
    t = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return '%02d:%02d:%02d'%(t, m, s)

cur_time = change_time2sec(list(map(int, sys.stdin.readline().split(':'))))
start_time = change_time2sec(list(map(int, sys.stdin.readline().split(':'))))

leave_time = start_time - cur_time if cur_time < start_time else 24*3600 + start_time - cur_time
print(change_sec2time(leave_time))