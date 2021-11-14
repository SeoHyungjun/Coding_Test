import sys

N = int(sys.stdin.readline())

star = [[' ']*(2*N-1) for _ in range(N)]

def make_star(x, y, size):
    if size == 3:
        star[x][y+2] = '*'
        star[x+1][y+1] = star[x+1][y+3] = '*'
        star[x+2][y] = star[x+2][y+1] = star[x+2][y+2] = star[x+2][y+3] = star[x+2][y+4] = '*'
    else:
        make_star(x, y+size//2, size//2)
        make_star(x+size//2, y, size//2)
        make_star(x+size//2, y+size, size//2)

make_star(0, 0, N)
for i in range(N):
    print(''.join(star[i]))