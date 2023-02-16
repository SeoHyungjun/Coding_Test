import sys

V = int(sys.stdin.readline())
vote = sys.stdin.readline()

if vote.count('A') > vote.count('B'):
    print('A')
elif vote.count('A') < vote.count('B'):
    print('B')
else:
    print('Tie')