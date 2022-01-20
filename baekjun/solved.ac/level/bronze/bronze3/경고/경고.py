import sys

h, m, s = map(int, sys.stdin.readline().rstrip().split(':'))
dh, dm, ds = map(int, sys.stdin.readline().rstrip().split(':'))

if ds - s >= 0:
    s = ds - s
else:
    s = ds - s + 60
    dm -= 1

if dm - m >= 0:
    m = dm - m 
else:
    m = dm - m + 60
    dh -= 1

if dh - h >= 0:
    h = dh - h 
else:
    h = dh - h + 24

if h == 0 and m == 0 and s == 0:
    h = 24

print('%02d:%02d:%02d'%(h, m, s))