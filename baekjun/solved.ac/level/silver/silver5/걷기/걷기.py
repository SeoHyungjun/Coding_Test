import sys

X, Y, W, S = map(int, sys.stdin.readline().split())

answer = []
# 모두 직선으로만 가는 경우
answer.append((X + Y)*W)

# 모두 대각선으로 2칸 /\같이 이동하는 경우, 홀수칸일 경우 한칸은 직선으로 이동
answer.append((X // 2 * 2 * S) + (X % 2 * W) + (Y // 2 * 2 * S) + (Y % 2 * W))

# 대각선으로 이동한 뒤 직선으로 이동
answer.append((min(X, Y) * S) + (max(X, Y) - min(X, Y)) * W)

# 대각선으로 이동한 뒤 직선을 대각선으로 이동
tmp = max(X, Y) - min(X, Y)
answer.append((min(X, Y) * S) + (tmp // 2 * 2 * S) + (tmp % 2 * W))

print(min(answer))