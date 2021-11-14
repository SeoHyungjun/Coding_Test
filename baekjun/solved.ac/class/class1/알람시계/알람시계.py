hh, mm = map(int, input().split())

if mm >= 45:
    mm -= 45
else:
    hh = (hh + 24 - 1)%24
    mm = (mm + 60 - 45)%60

print('{} {}'.format(hh, mm))