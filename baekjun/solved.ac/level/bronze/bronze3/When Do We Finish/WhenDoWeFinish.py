import sys

while True:
    start_time, add_time = sys.stdin.readline().split()
    if start_time == '00:00' and add_time == '00:00':
        break

    start_h, start_m = map(int, start_time.split(':'))
    add_h, add_m = map(int, add_time.split(':'))

    end_h, end_m = start_h + add_h, start_m + add_m
    if end_m > 59:
        end_h += 1
        end_m %= 60
    
    next_day = end_h // 24

    if next_day == 0:
        print('%02d:%02d'%(end_h, end_m))
    else:
        print('%02d:%02d +%d'%(end_h%24, end_m, next_day))