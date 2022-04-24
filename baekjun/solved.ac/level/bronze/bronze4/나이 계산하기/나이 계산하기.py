import sys

y1, m1, d1 = map(int, sys.stdin.readline().split())
y2, m2, d2 = map(int, sys.stdin.readline().split())

man_old = 0
if m1 < m2:
    man_old = y2-y1
elif m1 == m2:
    if d1 <= d2:
        man_old = y2-y1
    else:
        man_old = y2-y1-1
else:
    man_old = y2-y1-1
count_old = y2-y1+1
year_old = y2-y1

print(man_old)
print(count_old)
print(year_old)