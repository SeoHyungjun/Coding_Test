import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())

answer, exercise_time = 0, 0
cur_pulse = m

if m + T > M:
    print(-1)
else:
    while exercise_time < N:
        answer += 1

        if cur_pulse + T <= M:
            exercise_time += 1
            cur_pulse += T
        
        else:
            cur_pulse -= R
            if cur_pulse < m:
                cur_pulse = m

    print(answer)