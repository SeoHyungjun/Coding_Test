import sys

dic = {'black':	['0', ''], 
    'brown': ['1', '0'],
    'red' :	['2', '00'],
    'orange' :	['3', '000'],
    'yellow' :	['4', '0000'],
    'green'	: ['5', '00000'],
    'blue'	: ['6', '000000'],
    'violet' : ['7', '0000000'],
    'grey' : ['8', '00000000'],
    'white'	: ['9', '000000000']}

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()

print(int(dic[a][0] + dic[b][0] + dic[c][1]))