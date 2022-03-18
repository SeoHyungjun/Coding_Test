import sys

change = {'AA':'A', 'AG':'C', 'AC':'A', 'AT':'G', 'GA':'C', 'GG':'G', 'GC':'T', 'GT':'A', 'CA':'A', 'CG':'T', 'CC':'C', 'CT':'G', 'TA':'G', 'TG':'A', 'TC':'G', 'TT':'T'}

N = int(sys.stdin.readline())
DNA = sys.stdin.readline().rstrip()

answer = DNA[-1]
for i in range(N-1, -1, -1):
    answer = change[DNA[i] + answer]

print(answer)