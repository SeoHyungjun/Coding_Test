import sys

A, B = sys.stdin.readline().split()

print(sum(map(int, A)) * sum(map(int, B)))

"""
A = abc
B = fgh

af + ag + ah + bf + bg + bh + cf + cg + ch
= a(f + g + h) + b(f + g + g) + c(f + g + h)
= (a + b + c) * (f + g + h)
"""