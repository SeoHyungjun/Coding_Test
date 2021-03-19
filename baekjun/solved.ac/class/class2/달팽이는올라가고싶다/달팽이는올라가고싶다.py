a, b, v = map(int, input().split())

'''
(a - b) * n + a>= v
a - b * n >= v - a
n >= v-a / a-b
'''

print((v-a)//(a-b) + 1 if (v-a)%(a-b)==0 else (v-a)//(a-b)+2)