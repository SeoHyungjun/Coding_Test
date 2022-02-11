import sys

prev_temp = float(sys.stdin.readline())
while True:
    temp = float(sys.stdin.readline())

    if temp == 999:
        break

    print("%.2f"%(temp - prev_temp))
    prev_temp = temp