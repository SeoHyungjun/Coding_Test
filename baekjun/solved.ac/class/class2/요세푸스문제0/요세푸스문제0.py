answer = []

n, k = map(int, input().split())

circle = [i for i in range(1, n+1)]
index = 0 
while circle:
    index = (index + k-1) % len(circle)
    answer.append(str(circle.pop(index)))

print('<'+', '.join(answer)+'>')