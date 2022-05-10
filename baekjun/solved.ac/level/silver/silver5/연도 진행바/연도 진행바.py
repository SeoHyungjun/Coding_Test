import sys

month = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,\
        'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mon, day, year, t = sys.stdin.readline().split()
hour, minute = t.split(':')
day = day.replace(',', '')
year, day, hour, minute = map(int, [year, day, hour, minute])

if year % 400 == 0 or (year % 4 == 0 and year%100 != 0):
    day_of_month[1] += 1

total_time_to_min = sum(day_of_month) * 24 * 60

mon_to_day = sum(day_of_month[:month[mon]-1])
day_to_hour = (mon_to_day + day - 1) * 24
hour_to_min = (day_to_hour + hour) * 60

sum_time_to_min = hour_to_min + minute

print(sum_time_to_min/total_time_to_min*100)