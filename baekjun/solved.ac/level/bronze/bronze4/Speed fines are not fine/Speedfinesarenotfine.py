import sys

limit_speed = int(sys.stdin.readline())
cur_speed = int(sys.stdin.readline())

diff_speed = cur_speed - limit_speed
if diff_speed >= 31:
    fine = 500
elif diff_speed >= 21:
    fine = 270
elif diff_speed >= 1:
    fine = 100
else:
    fine = 0

if fine == 0:
    print('Congratulations, you are within the speed limit!')
else:
    print('You are speeding and your fine is $%d.'%(fine))