N, r, c = map(int, input().split())


def z_search(N, r, c, cnt):
    if N == 1:
        if r == 1 and c == 2:
            cnt += 1
        elif r == 2 and  c == 1:
            cnt += 2
        elif r == 2 and c == 2:
            cnt += 3
        return cnt

    else:
        if r > 2**(N-1):
            r -= 2**(N-1)
            cnt += (2**N) * (2**(N-1))
        if c > 2**(N-1):
            c -= 2**(N-1)
            cnt += (2**(N-1)) * (2**(N-1))

        return z_search(N-1, r, c, cnt)

print(z_search(N, r+1, c+1, 0))