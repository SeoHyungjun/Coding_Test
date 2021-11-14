import sys


def find_max_money(available_start_day, current_money):
    if available_start_day >= N:
        return current_money

    not_work_today = find_max_money(available_start_day + 1, current_money)
    max_money = not_work_today

    if available_start_day + schedule[available_start_day][0] <= N:
        work_today = find_max_money(available_start_day + schedule[available_start_day][0],
                                    current_money + schedule[available_start_day][1])
        max_money = max(max_money, work_today)

    return max_money


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(find_max_money(0, 0))