import sys
from functools import cmp_to_key

# ng를 c로 바꿔서 계산
minsik = {'a':0, 'b':1 , 'k':2, 'd':3, 'e':4, 'g':5, 'h':6, 'i':7, 'l':8, 'm':9, 'n':10, 'c':11, 'o':12, 'p':13, 'r':14, 's':15, 't':16, 'u':17, 'w':18, 'y':19}

def change_minsik(x, y):
    min_len = min(len(x), len(y))
    for i in range(min_len):
        if minsik[x[i]] > minsik[y[i]]:
            return 1
        elif minsik[x[i]] < minsik[y[i]]:
            return -1

    return -1 if len(x) < len(y) else 1

N = int(sys.stdin.readline())
input_string_list = []
for _ in range(N):
    input_string = sys.stdin.readline().rstrip()
    input_string_list.append(input_string.replace('ng', 'c'))

input_string_list.sort(key = cmp_to_key(change_minsik))
for i in range(N):
    print(input_string_list[i].replace('c', 'ng'))