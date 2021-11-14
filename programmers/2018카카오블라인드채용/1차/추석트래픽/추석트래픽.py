def solution(lines):
    answer = 0
    arr = []

    for line in lines:
        _, time, delay = line.split()
        h, m, s = time.split(':')
        delay = int(float(delay[:-1]) * 1000)

        end = int((int(h) * 3600 + int(m) * 60 + float(s)) * 1000)
        start = end - delay + 1
        
        arr.append((start, end))

    print(arr)

    for st, en in arr:
        st_cnt = 0
        en_cnt = 0
        for start, end in arr:
            #if not(end < st or start > st + 999):
            if (start <= st <= end or start <= st + 999 <= end) or (st < start and end < st+999):
                st_cnt += 1
            #if not(end < en or start > en + 999):
            if (start <= en <= end or start <= en + 999 <= end) or (en < start and end < en+999):
                en_cnt += 1

        if max(st_cnt, en_cnt) > answer:
            answer = max(st_cnt, en_cnt)

    return answer




lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))