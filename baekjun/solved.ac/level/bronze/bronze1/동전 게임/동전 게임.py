import sys

# 뒤뒤뒤,뒤뒤앞,뒤앞뒤,뒤앞앞,앞뒤뒤,앞뒤앞,앞앞뒤,앞앞앞
patterns = {'TTT':0, 'TTH':1, 'THT':2, 'THH':3, 'HTT':4, 'HTH':5, 'HHT':6, 'HHH':7}

N = int(sys.stdin.readline())
for _ in range(N):
    case = sys.stdin.readline().rstrip()

    answer = [0] * 8
    for i in range(38):
        answer[patterns[case[i:i+3]]] += 1

    print(*answer)