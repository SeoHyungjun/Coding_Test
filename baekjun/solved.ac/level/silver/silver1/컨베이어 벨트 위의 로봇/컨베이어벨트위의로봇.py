import sys
from collections import deque


def move_belt():
    global belt
    robot = deque([False] * N)
    answer = 0
    cnt_zero = 0

    while True:
        answer += 1

        # 벨트 회전
        belt.rotate(1)
        robot.rotate(1)
        robot[N-1] = False

        # 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] and not robot[i+1] and belt[i+1] > 0:
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    cnt_zero += 1
                robot[i+1] = True
                robot[i] = False
        # 내려가는 위치의 로봇 내리기
        robot[N-1] = False
        # 올리는 위치에 로봇 올리기
        if belt[0] > 0 and not robot[0]:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                cnt_zero += 1

        # 내구도0이 k개 이상인지 확인
        if cnt_zero >= K:
            break

    return answer


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    belt = deque(list(map(int, sys.stdin.readline().split())))
    print(move_belt())