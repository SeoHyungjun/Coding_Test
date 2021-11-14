import sys
HEIGHT, CNT = 0, 1

def solve():
    stack = []
    answer = 0

    for h in arr:
        # stack에 현재 사람보다 작은 사람이 있으면 pop하고 answer에 추가
        while stack and stack[-1][HEIGHT] < h:
            answer += stack.pop()[CNT]

        # 스택이 비었으면 현재 사람을 그냥 추가
        if not stack:
            stack.append((h, 1))
            continue

        # 스택이 안 비었고, top과 지금 현재 사람의 키가 같으면
        if stack[-1][HEIGHT] == h:
            cnt = stack.pop()[CNT]
            answer += cnt

            # 현재 같은키보다 왼쪽이 있으므로 -> top과 현재 사람이 볼 수 있으므로 1추가
            if stack:
                answer += 1

            # 현재 키인 사람과 같은 사람이 cnt만큼 있으므로, 키 = h, 명수 = cnt+1를 스택에 추가
            stack.append((h, cnt + 1))

        # 스택이 안비었고, 왼쪽 사람보다 키가 작으므로 그 사람만 볼 수 있음 -> 스택에 현재 키를 넣고, answer에 1추가(왼쪽 사람만 볼 수 있으므로)
        else:
            stack.append((h, 1))
            answer += 1

    return answer 

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
print(solve())
