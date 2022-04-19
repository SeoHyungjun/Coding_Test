import sys

T = int(sys.stdin.readline())

for _ in range(T):
    _ = sys.stdin.readline()
    N, M = map(int, sys.stdin.readline().split())
    c_language_class = list(map(int, sys.stdin.readline().split()))
    economics_class = list(map(int, sys.stdin.readline().split()))

    c_avg = sum(c_language_class)/N
    e_avg = sum(economics_class)/M

    can_move = [c for c in c_language_class if c < c_avg and c > e_avg]

    print(len(can_move))