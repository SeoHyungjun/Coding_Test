from collections import deque

n = int(input())

card = deque([i for i in range(1, n+1)])

while n > 1:
    # 맨 위 카드 버리기
    card.popleft()

    # 다음 맨 위카드를 맨 뒤로
    card.append(card.popleft())
    n -= 1

print(card[0])
