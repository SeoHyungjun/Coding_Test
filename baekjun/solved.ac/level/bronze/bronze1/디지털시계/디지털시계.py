import sys

def add_one_sec(t):
    h, m, s = map(int, t.split(':'))

    s += 1
    if s >= 60:
        s %= 60
        m += 1
    if m >= 60:
        m %= 60
        h += 1

    return '%02d:%02d:%02d'%(h, m, s)

def time2int(t):
    return int(''.join(t.split(':')))

for _ in range(3):
    st, en = sys.stdin.readline().split()
    cur = st

    if time2int(cur) > time2int(en):
        h, m, s = map(int, en.split(':'))
        en = '%02d:%02d:%02d'%(h + 24, m, s)

    end_int_time = time2int(en)

    answer = 0
    while True:
        int_time = time2int(cur)
        if int_time > end_int_time:
            break
        if int_time % 3 == 0:
            answer += 1
        cur = add_one_sec(cur)

    print(answer)