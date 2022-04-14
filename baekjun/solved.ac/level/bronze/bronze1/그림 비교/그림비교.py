import sys

class picture:
    def __init__(self, pic) -> None:
        self.pic = pic

    def compare(self, other):
        diff = 0

        for i in range(5):
            for j in range(7):
                if self.pic[i][j] != other.pic[i][j]:
                    diff += 1

        return diff

N = int(sys.stdin.readline())
pictures = []

for _ in range(N):
    cur_picture = [sys.stdin.readline().rstrip() for _ in range(5)]
    pictures.append(picture(cur_picture))

min_diff = float('inf')
a, b = 0, 0
for i in range(N):
    for j in range(i+1, N):
        cur_diff = pictures[i].compare(pictures[j])
        if cur_diff < min_diff:
            min_diff = cur_diff
            a, b = i, j

print(a+1, b+1)