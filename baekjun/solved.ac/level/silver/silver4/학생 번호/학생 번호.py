import sys

N = int(sys.stdin.readline())
student_id = [sys.stdin.readline().rstrip() for _ in range(N)]
len_student_id = len(student_id[0])

for i in range(1, len_student_id + 1):
    num_set = set()
    for id in student_id:
        int_student_id = int(id[-i:])
        if int_student_id in num_set:
            break

        num_set.add(int_student_id)

    if len(num_set) == N:
        print(i)
        break