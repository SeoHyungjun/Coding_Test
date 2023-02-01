import sys

ball = [1, 2, 3, 4]

str = sys.stdin.readline()
for c in str:
    if c == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif c == 'B':
        ball[0], ball[2] = ball[2], ball[0]
    elif c == 'C':
            ball[0], ball[3] = ball[3], ball[0]
    elif c == 'D':
            ball[1], ball[2] = ball[2], ball[1]
    elif c == 'E':
            ball[1], ball[3] = ball[3], ball[1]
    elif c == 'F':
            ball[2], ball[3] = ball[3], ball[2]

print(ball.index(1) + 1)
print(ball.index(4) + 1)