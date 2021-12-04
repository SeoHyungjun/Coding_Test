import sys

time_arr = [int(sys.stdin.readline()) for _ in range(5)]

if time_arr[0] < 0:
    answer = time_arr[2] * abs(time_arr[0]) + time_arr[3] + time_arr[1] * time_arr[4]
elif time_arr[0] == 0:
    answer = time_arr[3] + time_arr[1] * time_arr[4]
else:
    answer = (time_arr[1] - time_arr[0]) * time_arr[4]

print(answer)