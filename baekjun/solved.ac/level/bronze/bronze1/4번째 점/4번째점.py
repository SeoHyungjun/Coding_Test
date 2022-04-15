import sys

while True:
    try:
        arr = list(map(float, sys.stdin.readline().split()))

        a = (arr[0], arr[1])
        b = (arr[2], arr[3])
        c = (arr[4], arr[5])
        d = (arr[6], arr[7])

        if a == c:
            a, b = b, a
        elif a == d:
            a, b, c, d = b, a, d, c
        elif b == c:
            pass
        else:
            c, d = d, c
        
        e = (d[0] - (b[0] - a[0]), d[1] - (b[1] - a[1]))
        print("%0.3f %0.3f"%(e[0], e[1]))

    except:
        break