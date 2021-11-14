import sys

hometoschool = int(sys.stdin.readline())
schooltopc = int(sys.stdin.readline())
pctocram = int(sys.stdin.readline())
cramtohome = int(sys.stdin.readline())

totalsec = hometoschool + schooltopc + pctocram + cramtohome

print(totalsec//60, totalsec%60, sep = '\n')