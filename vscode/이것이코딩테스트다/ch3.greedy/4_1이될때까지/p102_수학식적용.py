N, K = map(int, input().split())

# 연산 된 횟수 확인
count = 0

while True:
    # (N//K) * K -> 몫 * K 이므로 K의 배수 중 N에 가장 가까운 수를 구함
    near = (N//K) *K
    # 1씩 빼는 연산이 N - near 만큼 반복
    count += N - near
    # N 에서 1씩 N-near번 만큼 뺐으므로, N은 near이 됨
    N = near

    # n이 K보다 작을 경우 더 이상 나눌 수 없으므로 반복문 탈출
    if N < K:
        break

    # n이 K로 나눠지므로 나누고 count 증가
    count += 1
    N //= K

# n은 K보다 작은 수이므로 1씩 빼서 1을 만들어야 함, 즉 n-1번 반복해야 1이 됨
count += N-1
print(count)