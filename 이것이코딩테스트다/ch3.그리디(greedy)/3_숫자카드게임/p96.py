# 행, 열 입력
N, M = map(int, input().split())

# 각 카드의 값을 저장할 card 리스트 생성
card = []
# 행의 최소값들 중 가장 큰 수를 저장 할 변수 생성
min_card_num = 0

# 각 행별로 하나씩 확인해야하므로 for문의 크기는 N
# 각 카드의 데이터를 저장하지 않아도 상관 없음
for i in range(N):
    # 각 카드의 숫자를 2중 리스트 형태로 저장
    card.append( list(map(int, input().split())) )
    # 각 행의 카드 중 최소값을 최소값들 중 가장 큰 수를 저장하는 변수와 비교
    # 만약 지금 행의 최소값이 이전 행들의 최소값보다 크다면 교체
    if min_card_num < min(card[i]):
        min_card_num = min(card[i])

print(min_card_num)