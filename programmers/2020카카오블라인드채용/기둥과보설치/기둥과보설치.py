# 2021-03-07 16:34 -> 17:38 +++ 18:09 -> 18:26 
# 해설 보고 풀었음... 매우 어렵 ㅠ

def check(ans):
    for x, y, a in ans:
        # 기둥일 때
        if a == 0:
            # 바닥이거나, 아래 기둥이 있거나, 한칸 왼쪽에서 보가 시작하거나, 아래에서 보가 시작하거나
            if y == 0 or [x, y-1, 0] in ans or [x-1, y, 1] in ans or [x, y, 1] in ans:
                continue
            else:
                return False
        # 보 일때
        else:
            # 왼쪽이 기둥이거나, 오른쪽이 기둥이거나, 양쪽이 보거나
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ( [x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False

    return True

def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        # b == 1 -> 설치 
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove(([x, y, a]))

        # b == 0 -> 삭제
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    return sorted(answer)


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))
