import sys

grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F':0.0}

N = int(sys.stdin.readline())
grade_sum = 0
grade_cnt = 0
for _ in range(N):
    _, g, n = sys.stdin.readline().rstrip().split()

    grade_sum += int(g) * grade[n]
    grade_cnt += int(g)

print('%.2f'%(grade_sum/grade_cnt + 0.000000000001))